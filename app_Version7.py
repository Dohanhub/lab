import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

st.set_page_config(layout="wide", page_title="SRL Automation Data Explorer")

# ---- Sidebar Navigation ----
def sidebar_navigation():
    st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=150)
    st.sidebar.title("Navigation")
    nav = st.sidebar.radio(
        "Go to",
        [
            "🏠 Home",
            "📖 Introduction",
            "💬 Chat / LLM",
            "🔎 Main Insights",
            "🧭 Info / What’s Introduced",
            "📊 Data Analysis",
            "🚪 Exit"
        ]
    )
    return nav

# ---- Home/Cover Page ----
def home_page():
    st.title("🏠 Welcome to SRL Automation Data Explorer")
    st.markdown("""
    <div style='font-size:22px;'>
    <p>
    <b>SRL Automation Data Explorer</b> is your intelligent hub for interactive data analysis, machine learning, and actionable business insights.
    </p>
    <ul>
      <li>Visualize and interrogate your data in real time</li>
      <li>Run advanced analytics and ML with a click</li>
      <li>Chat with your data using Language Models (LLMs)</li>
      <li>Export insights and models for downstream use</li>
    </ul>
    <br>
    <i>Select a section from the sidebar to get started!</i>
    </div>
    """, unsafe_allow_html=True)

# ---- Introduction Page ----
def intro_page():
    st.title("📖 Introduction & Story")
    st.markdown("""
    Welcome to the SRL Automation Data Explorer, a next-generation platform designed for analysts, data scientists, and business users.
    <br><br>
    **Story:**<br>
    Born out of the need to simplify and accelerate analytics, this dashboard brings together automated data profiling, powerful ML, and seamless explainability—all in one place. Whether you’re a data novice or an expert, you can uncover answers and trends in seconds.
    <br><br>
    **How to use:**<br>
    - Use the sidebar to navigate between Home, Introduction, Chat/LLM, Insights, Info, and Data Analysis.
    - Upload or select your data for exploration in the Data Analysis section.
    - Try out the Chat/LLM section to interact with your data conversationally (beta).
    """, unsafe_allow_html=True)

# ---- Chat/LLM Page ----
def chat_llm_page():
    st.title("💬 Chat / LLM (Language Model)")
    st.info("This page is reserved for conversational analytics and LLM integration. Coming soon!")
    st.write("You will be able to ask questions about your data, generate summaries, and more via natural language.")

# ---- Main Insights Page ----
def main_insights_page(df):
    st.title("🔎 Main Insights")
    if df is None or df.empty:
        st.warning("No data loaded. Please upload/select a data file in the Data Analysis section.")
        return
    # Example: Main insights cards
    st.header("Headline KPIs")
    numeric_cols = df.select_dtypes(include=np.number).columns
    st.write("Total Rows:", df.shape[0])
    st.write("Total Columns:", df.shape[1])
    if len(numeric_cols) > 0:
        st.metric("Average of first numeric column", f"{df[numeric_cols[0]].mean():,.2f}")
        st.metric("Max of first numeric column", f"{df[numeric_cols[0]].max():,.2f}")
    else:
        st.info("No numeric columns for KPI cards.")
    st.write("**Top 5 columns by number of missing values:**")
    st.write(df.isnull().sum().sort_values(ascending=False).head())

# ---- Info/What Will Be Introduced Page ----
def info_page():
    st.title("🧭 Info / What Will Be Introduced")
    st.markdown("""
    **This dashboard offers:**
    - Interactive data exploration (Overview, Column Analysis, Relationships, ML, and more)
    - 4-way sample analysis for any column
    - Export of models and predictions
    - LLM/Chat integration (coming soon)
    - Headline insights and KPIs
    - Easy sidebar navigation with Home, Info, and Exit
    """)
    st.markdown("**We aim to introduce:**")
    st.markdown("""
    - Automated report generation
    - Live collaboration and annotation
    - More AI-powered insights and anomaly detection
    """)

# ---- Data Loader ----
def load_data(file):
    ext = os.path.splitext(file)[1].lower()
    if ext in [".xlsx", ".xls"]:
        return pd.read_excel(file)
    elif ext in [".csv"]:
        return pd.read_csv(file)
    else:
        st.error("Unsupported file type!")
        return None

# ---- Data Analysis/5 Tabs ----
def data_analysis_page():
    st.title("📊 Data Analysis & ML")
    folder = st.sidebar.text_input("Data Folder Path", value=".")
    files = [os.path.join(folder, f) for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(('.csv', '.xlsx', '.xls'))]
    if not files:
        st.warning("No CSV or Excel files found in the folder.")
        return None
    file = st.sidebar.selectbox("Select file", files)
    df = load_data(file)
    if df is None:
        return None

    # --- Tabbed Navigation for Analysis ---
    tabs = st.tabs([
        "Overview",
        "Column Analysis",
        "Relationship Analysis",
        "ML & Explainability",
        "4-Graphic Column Analyzer"
    ])
    with tabs[0]:
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
    with tabs[1]:
        column_analysis_tab(df)
    with tabs[2]:
        relationship_analysis_tab(df)
    with tabs[3]:
        ml_explain_tab(df)
    with tabs[4]:
        four_graphic_column_tab(df)
    return df

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

# --- Tab 2: Column Analysis ---
def column_analysis_tab(df):
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
def relationship_analysis_tab(df):
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
def ml_explain_tab(df):
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
def four_graphic_column_tab(df):
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

# ---- Exit Page ----
def exit_page():
    st.title("🚪 Exit")
    st.success("Thank you for using the SRL Automation Data Explorer!")
    st.stop()

# ---- Main Controller ----
def main():
    nav = sidebar_navigation()
    # Store last-used DataFrame for insights
    if 'last_df' not in st.session_state:
        st.session_state.last_df = None
    if nav == "🏠 Home":
        home_page()
    elif nav == "📖 Introduction":
        intro_page()
    elif nav == "💬 Chat / LLM":
        chat_llm_page()
    elif nav == "🔎 Main Insights":
        main_insights_page(st.session_state.last_df)
    elif nav == "🧭 Info / What’s Introduced":
        info_page()
    elif nav == "📊 Data Analysis":
        st.session_state.last_df = data_analysis_page()
    elif nav == "🚪 Exit":
        exit_page()

if __name__ == "__main__":
    main()