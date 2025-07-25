import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, IsolationForest
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

st.set_page_config(layout="wide")

try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False

try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False

def load_data(file):
    ext = os.path.splitext(file)[1].lower()
    if ext in [".xlsx", ".xls"]:
        return pd.read_excel(file)
    elif ext in [".csv"]:
        return pd.read_csv(file)
    else:
        st.error("Unsupported file type!")
        return None

def kpi_section(df):
    st.subheader("Key Performance Indicators (KPIs)")
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        st.metric(f"{col} mean", f"{df[col].mean():.2f}")
        st.metric(f"{col} median", f"{df[col].median():.2f}")
        st.metric(f"{col} min", f"{df[col].min():.2f}")
        st.metric(f"{col} max", f"{df[col].max():.2f}")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        top = df[col].value_counts().head(1)
        if not top.empty:
            st.metric(f"{col} top", f"{top.index[0]} ({top.iloc[0]})")

def show_overall(df):
    st.title("📊 Advanced Data Explorer")
    st.write("## Dataset Preview")
    st.dataframe(df.head(20))
    st.write("### Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.write("### Data Types")
    st.write(df.dtypes)
    st.write("### Missing Values")
    st.write(df.isnull().sum())
    kpi_section(df)
    st.write("### Descriptive Statistics")
    st.write(df.describe(include='all'))

def visualize_column(df, col):
    st.write(f"## Column: {col}")
    dtype = df[col].dtype
    st.write(f"Type: {dtype}")

    if pd.api.types.is_numeric_dtype(df[col]):
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        st.pyplot(fig)
        st.write(df[col].describe())
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        st.pyplot(fig)
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        st.line_chart(df.set_index(col).resample("D").size())
    else:
        counts = df[col].value_counts().head(20)
        st.bar_chart(counts)
        st.write(counts)

    st.write("### Missing values:", df[col].isnull().sum())

def visualize_relationship(df, col1, col2):
    st.write(f"## Relationship: {col1} vs {col2}")
    if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
        st.pyplot(fig)
        fig, ax = plt.subplots()
        sns.regplot(x=df[col1], y=df[col2], ax=ax, line_kws={"color": "red"})
        st.pyplot(fig)
        st.write(df[[col1, col2]].corr())
    else:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col1], y=df[col2], ax=ax)
        st.pyplot(fig)

def advanced_visuals(df):
    st.subheader("Advanced Visualizations")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 1:
        st.write("### Pairplot")
        cols = st.multiselect("Select up to 4 numeric columns for pairplot", num_cols, default=list(num_cols)[:2])
        if 1 < len(cols) <= 4:
            fig = sns.pairplot(df[cols].dropna())
            st.pyplot(fig)
        st.write("### Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

def anomaly_detection(df):
    st.subheader("Anomaly Detection (Isolation Forest)")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) == 0:
        st.info("No numeric columns for anomaly detection.")
        return
    feature = st.selectbox("Select column for anomaly detection", num_cols)
    contamination = st.slider("Expected Outlier Fraction", 0.01, 0.3, 0.05, 0.01)
    X = df[[feature]].dropna()
    model = IsolationForest(contamination=contamination, random_state=42)
    preds = model.fit_predict(X)
    outliers = X[preds == -1]
    st.write(f"Detected {outliers.shape[0]} anomalies in {feature}.")
    fig, ax = plt.subplots()
    sns.histplot(df[feature], kde=True, ax=ax, color="blue", label="All data")
    sns.scatterplot(x=outliers[feature], y=[0]*len(outliers), ax=ax, color="red", label="Anomalies")
    plt.legend()
    st.pyplot(fig)
    st.write(outliers)

def clustering(df):
    st.subheader("Clustering (KMeans)")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) < 2:
        st.info("Need at least 2 numeric columns for clustering.")
        return
    cols = st.multiselect("Select columns for clustering", num_cols, default=list(num_cols)[:2])
    k = st.slider("Number of clusters", 2, 8, 3)
    X = df[cols].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    Xc = X.copy()
    Xc["Cluster"] = labels
    if len(cols) == 2:
        fig, ax = plt.subplots()
        sns.scatterplot(x=Xc[cols[0]], y=Xc[cols[1]], hue=Xc["Cluster"], palette="tab10", ax=ax)
        st.pyplot(fig)
    st.write(Xc.head())

def forecasting(df):
    st.subheader("Forecasting (Prophet)")
    if not PROPHET_AVAILABLE:
        st.warning("Prophet not installed. Run `pip install prophet`.")
        return
    date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    num_cols = df.select_dtypes(include='number').columns
    if not date_cols or not num_cols.any():
        st.info("Need at least one datetime and one numeric column.")
        return
    date_col = st.selectbox("Select datetime column", date_cols)
    value_col = st.selectbox("Select value column", num_cols)
    horizon = st.slider("Forecast days", 7, 365, 30)
    dff = df[[date_col, value_col]].dropna()
    dff = dff.sort_values(date_col)
    dff = dff.rename(columns={date_col: "ds", value_col: "y"})
    m = Prophet()
    m.fit(dff)
    future = m.make_future_dataframe(periods=horizon)
    forecast = m.predict(future)
    fig1 = m.plot(forecast)
    st.pyplot(fig1)
    st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(horizon))

def ml_and_explain(df):
    st.subheader("ML & Explainability")
    st.write("Select a target column for supervised learning. The app will auto-detect classification vs regression.")
    target = st.selectbox("Target column", df.columns)
    drop_cols = st.multiselect("Columns to drop (e.g., IDs, leaks)", [])
    x_df = df.drop(columns=[target] + drop_cols)
    y = df[target]
    x_df = pd.get_dummies(x_df, drop_first=True)
    mask = y.notnull()
    x_df, y = x_df[mask], y[mask]
    clf_task = pd.api.types.is_object_dtype(y) or pd.api.types.is_categorical_dtype(y)
    if clf_task:
        y_enc = LabelEncoder().fit_transform(y)
        y_out = y_enc
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        y_out = y
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    test_size = st.slider("Test size", 0.1, 0.5, 0.2)
    X_train, X_test, y_train, y_test = train_test_split(x_df, y_out, test_size=test_size, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    st.write(f"Feature count after encoding: {x_df.shape[1]}")
    st.write("### Model Results")
    if clf_task:
        st.write(f"**Accuracy:** {accuracy_score(y_test, y_pred):.3f}")
        st.write("**Classification Report:**")
        st.text(classification_report(y_test, y_pred))
        st.write("**Confusion Matrix:**")
        fig, ax = plt.subplots()
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues", ax=ax)
        st.pyplot(fig)
    else:
        st.write(f"**MAE:** {mean_absolute_error(y_test, y_pred):.3f}")
        st.write(f"**RMSE:** {mean_squared_error(y_test, y_pred):.3f}")
        st.write(f"**R²:** {r2_score(y_test, y_pred):.3f}")
        fig, ax = plt.subplots()
        sns.scatterplot(x=y_test, y=y_pred, ax=ax)
        ax.set_xlabel("True")
        ax.set_ylabel("Predicted")
        st.pyplot(fig)
    st.write("### Feature Importances")
    importances = model.feature_importances_
    feat_imp = pd.Series(importances, index=x_df.columns).sort_values(ascending=False).head(20)
    st.bar_chart(feat_imp)
    if SHAP_AVAILABLE:
        st.write("### SHAP Explainability")
        explainer = shap.Explainer(model, X_train)
        shap_values = explainer(X_test)
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, X_test, show=False)
        st.pyplot(fig)
    else:
        st.info("Install SHAP for explainability: pip install shap")
    # Export model
    import joblib
    import io
    buffer = io.BytesIO()
    joblib.dump(model, buffer)
    st.download_button(
        label="Download trained model (.pkl)",
        data=buffer.getvalue(),
        file_name="trained_model.pkl"
    )
    # Export predictions
    pred_df = pd.DataFrame({"y_true": y_test, "y_pred": y_pred})
    st.download_button(
        label="Download predictions (.csv)",
        data=pred_df.to_csv(index=False),
        file_name="predictions.csv"
    )

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

    tabs = st.tabs([
        "Overview", "Advanced Visuals", "Column Explorer", "Relationship Explorer",
        "Anomaly Detection", "Clustering", "Forecasting", "ML & Explainability"
    ])
    with tabs[0]:
        show_overall(df)
    with tabs[1]:
        advanced_visuals(df)
    with tabs[2]:
        col = st.selectbox("Choose a column to analyze", df.columns)
        visualize_column(df, col)
    with tabs[3]:
        col1 = st.selectbox("Column 1", df.columns, key="rel1")
        col2 = st.selectbox("Column 2", df.columns, key="rel2")
        if col1 != col2:
            visualize_relationship(df, col1, col2)
    with tabs[4]:
        anomaly_detection(df)
    with tabs[5]:
        clustering(df)
    with tabs[6]:
        forecasting(df)
    with tabs[7]:
        ml_and_explain(df)

if __name__ == "__main__":
    main()