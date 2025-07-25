import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")

# --- Load Data ---
def load_data(file):
    ext = os.path.splitext(file)[1].lower()
    if ext in [".xlsx", ".xls"]:
        return pd.read_excel(file)
    elif ext in [".csv"]:
        return pd.read_csv(file)
    else:
        st.error("Unsupported file type!")
        return None

# --- KPI Cards ---
def display_kpi_cards(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    n_rows, n_cols = df.shape
    st.markdown("### 📊 Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", n_rows)
    col2.metric("Columns", n_cols)
    col3.metric("Numeric Cols", len(numeric_cols))
    col4.metric("Total Nulls", int(df.isnull().sum().sum()))

# --- Tab 1: Overview ---
def tab_overview(df):
    display_kpi_cards(df)
    st.markdown("---")
    st.header("Table Columns & Types")
    data_types = pd.DataFrame({
        'Column': df.columns,
        'Data Type': [str(df[c].dtype) for c in df.columns]
    })
    st.dataframe(data_types, use_container_width=True)
    st.header("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)
    st.header("Descriptive Statistics")
    st.dataframe(df.describe(include='all').T, use_container_width=True)

# --- Tab 2: Column Analysis ---
def tab_column_analysis(df):
    st.header("Column Analysis")
    col = st.selectbox("Select a column for analysis", df.columns)
    if pd.api.types.is_numeric_dtype(df[col]):
        st.subheader("Histogram")
        fig1, ax1 = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax1, color="skyblue")
        st.pyplot(fig1)
        st.subheader("Boxplot")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[col].dropna(), ax=ax2, color="lightgreen")
        st.pyplot(fig2)
        st.subheader("Stats")
        st.write(df[col].describe())
    else:
        st.subheader("Top Values")
        vc = df[col].value_counts().head(10)
        st.bar_chart(vc)
        st.write(vc)
        st.subheader("Unique Values")
        st.write(df[col].nunique())
    st.subheader("Missing Values")
    n_missing = df[col].isnull().sum()
    st.write(f"{n_missing} missing ({n_missing/len(df)*100:.1f}%)")

# --- Tab 3: Relationship Analysis ---
def tab_relationship_analysis(df):
    st.header("Relationship Analysis")
    num_cols = df.select_dtypes(include=np.number).columns
    if len(num_cols) < 2:
        st.info("Need at least 2 numeric columns for analysis.")
        return
    col1 = st.selectbox("Column 1", num_cols, key="rel1")
    col2 = st.selectbox("Column 2", num_cols, key="rel2")
    if col1 != col2:
        st.subheader("Scatterplot")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
        st.pyplot(fig)
        st.subheader("Correlation")
        st.write(df[[col1, col2]].corr())
        st.subheader("Regression Plot")
        fig2, ax2 = plt.subplots()
        sns.regplot(x=df[col1], y=df[col2], ax=ax2, line_kws={"color": "red"})
        st.pyplot(fig2)
    st.subheader("Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

# --- Tab 4: ML & Explainability ---
def tab_ml_explain(df):
    st.header("ML & Explainability")
    target = st.selectbox("Target column", df.columns)
    drop_cols = st.multiselect("Columns to drop (e.g., IDs, leaks)", [])
    x_df = df.drop(columns=[target] + drop_cols)
    y = df[target]
    x_df = pd.get_dummies(x_df, drop_first=True)
    mask = y.notnull()
    x_df, y = x_df[mask], y[mask]
    clf_task = pd.api.types.is_object_dtype(y) or pd.api.types.is_categorical_dtype(y)
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.preprocessing import LabelEncoder
    if clf_task:
        y_enc = LabelEncoder().fit_transform(y)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        y_out = y_enc
    else:
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        y_out = y
    test_size = st.slider("Test size", 0.1, 0.5, 0.2)
    X_train, X_test, y_train, y_test = train_test_split(x_df, y_out, test_size=test_size, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    if clf_task:
        from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
        st.write(f"**Accuracy:** {accuracy_score(y_test, y_pred):.3f}")
        st.text(classification_report(y_test, y_pred))
        fig, ax = plt.subplots()
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues", ax=ax)
        st.pyplot(fig)
    else:
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        st.write(f"**MAE:** {mean_absolute_error(y_test, y_pred):.3f}")
        st.write(f"**RMSE:** {mean_squared_error(y_test, y_pred, squared=False):.3f}")
        st.write(f"**R²:** {r2_score(y_test, y_pred):.3f}")
        fig, ax = plt.subplots()
        sns.scatterplot(x=y_test, y=y_pred, ax=ax)
        ax.set_xlabel("True")
        ax.set_ylabel("Predicted")
        st.pyplot(fig)
    st.subheader("Feature Importances")
    importances = model.feature_importances_
    feat_imp = pd.Series(importances, index=x_df.columns).sort_values(ascending=False).head(20)
    st.bar_chart(feat_imp)

# --- Tab 5: 4-Graphic Column Analyzer ---
def tab_4graphic_column(df):
    st.header("4-Graphic Analyzer for a Column")
    col = st.selectbox("Select a column for 4-way analysis", df.columns)
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    # 1. Histogram (if numeric)
    with c1:
        st.subheader("Distribution")
        if pd.api.types.is_numeric_dtype(df[col]):
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), kde=True, ax=ax, color="skyblue")
            st.pyplot(fig)
        else:
            st.info("Not numeric: Skipping histogram.")

    # 2. Boxplot (if numeric)
    with c2:
        st.subheader("Boxplot")
        if pd.api.types.is_numeric_dtype(df[col]):
            fig, ax = plt.subplots()
            sns.boxplot(x=df[col].dropna(), ax=ax, color="lightgreen")
            st.pyplot(fig)
        else:
            st.info("Not numeric: Skipping boxplot.")

    # 3. Value counts (for categorical or all)
    with c3:
        st.subheader("Top Values")
        vc = df[col].value_counts().head(10)
        st.bar_chart(vc)
        st.write(vc)

    # 4. Missing Values & Stats
    with c4:
        st.subheader("Missing & Stats")
        n_missing = df[col].isnull().sum()
        st.write(f"**Missing values:** {n_missing} ({n_missing/len(df)*100:.1f}%)")
        if pd.api.types.is_numeric_dtype(df[col]):
            st.write(df[col].describe())
        else:
            st.write(f"**Unique values:** {df[col].nunique()}")

# --- Main ---
def main():
    st.sidebar.title("Data File Selection")
    folder = st.sidebar.text_input("Folder path", value=".")
    files = [os.path.join(folder, f) for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(('.csv', '.xlsx', '.xls'))]
    if not files:
        st.warning("No CSV or Excel files found in the folder.")
        return
    file = st.sidebar.selectbox("Select file", files)
    df = load_data(file)
    if df is None:
        return

    # --- Tabbed Navigation ---
    tabs = st.tabs([
        "Overview",
        "Column Analysis",
        "Relationship Analysis",
        "ML & Explainability",
        "4-Graphic Column Analyzer"
    ])
    with tabs[0]:
        tab_overview(df)
    with tabs[1]:
        tab_column_analysis(df)
    with tabs[2]:
        tab_relationship_analysis(df)
    with tabs[3]:
        tab_ml_explain(df)
    with tabs[4]:
        tab_4graphic_column(df)

if __name__ == "__main__":
    main()