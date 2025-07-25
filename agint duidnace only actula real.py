howi  it iwll have actual data i have to feed all tupes of data and thr app must integratt all together and presnt all data i ahvae added in smoth soorealn DoganLab Business Intelligence Application (Streamlit)
This Streamlit application is designed for enterprise‑grade business intelligence, analytics, and AI assistance tailored to the Saudi market. It provides a modular architecture with multiple functional components, including dashboards, KPI analytics, advanced modeling, proposal generation, portfolio scorecards, a conversational AI copilot, and an admin panel.
Key features
•	Data first: The app does not ship with example data. Instead, it requires you to upload your own dataset (CSV format) via the sidebar. All analyses, charts, and models operate on the data you provide.
•	Multi‑language support: English and Arabic translations are available for UI labels. Additional languages can be added by extending the TRANSLATIONS dictionary.
•	Modular design: Each functional area of the BI system is encapsulated in its own function. This makes the code easier to maintain and extend. A navigation radio button in the sidebar allows switching between modules.
•	Advanced analytics: Includes a simple machine learning pipeline using scikit‑learn to train and evaluate a model on your dataset. Hyperparameters and target/feature selections are exposed through Streamlit widgets. The pipeline can be replaced or extended to use other algorithms such as CatBoost or XGBoost when those libraries are installed.
•	Proposal generator: Generates client proposals using a configurable template. The template can be customised and enriched with AI services (e.g. OpenAI) when appropriate API keys are supplied.
•	AI copilot: Provides a chat‑like interface for natural language queries. This implementation contains a placeholder stub that illustrates the flow; you must integrate it with your preferred large language model (LLM) back end for production use.
To run the app locally, make sure you have Streamlit installed (pip install streamlit) and execute: streamlit run doganlab_bi_app.py. """
from future import annotations
import json import os from typing import Dict, Optional, Tuple
import numpy as np import pandas as pd
import streamlit as st
Optional imports for machine learning. These may need to be installed
in your environment. If they are missing, the advanced analytics
module will display a friendly warning.
try: from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier from sklearn.metrics import mean_squared_error, r2_score, accuracy_score from sklearn.model_selection import train_test_split from sklearn.preprocessing import LabelEncoder except ImportError: RandomForestRegressor = None # type: ignore RandomForestClassifier = None # type: ignore
###############################################################################
Translation support
###############################################################################
Define translation dictionaries for supported languages. UI strings are
looked up using keys; if a translation is missing, the English
fallback is used. To add another language, copy the English keys and
provide translations for each value.
TRANSLATIONS: Dict[str, Dict[str, str]] = { "en": { "language": "Language", "welcome": "Welcome", "select_module": "Select Module", "dashboard": "Dashboard", "kpi_analytics": "KPI Analytics", "advanced_analytics": "Advanced Analytics", "proposal_generator": "Proposal Generator", "portfolio_scorecard": "Portfolio Scorecard", "ai_copilot": "AI Copilot", "admin_panel": "Admin Panel", "logout": "Logout", "upload_data": "Upload your data (CSV)", "no_data": "Please upload a CSV file to begin.", "total_records": "Total Records", "average_value": "Average Value", "max_value": "Max Value", "advanced_modeling": "Modeling with Random Forest", "select_target": "Select target column", "select_features": "Select feature columns", "train_model": "Train Model", "model_results": "Model Results", "proposal_heading": "Generate Proposal", "client_name": "Client name", "project_scope": "Project scope", "generate_proposal": "Generate proposal", "proposal_output": "Proposal output", "chat_with_ai": "Chat with AI about your data", "enter_question": "Enter your question", "send": "Send", "settings": "Settings", "upload_success": "File uploaded successfully.", "sales_analytics": "Sales & Pre‑Sales Analytics", "select_sales_amount": "Select sales amount column", "select_stage": "Select stage column", "select_outcome": "Select outcome column", "won_label": "Label for won deals", "funnel_title": "Sales Funnel by Stage", "win_rate": "Win rate", "sales_by_stage": "Sales by stage", "sales_total": "Total sales", "average_deal_size": "Average deal size", "won_deals": "Won deals", "lost_deals": "Lost deals", "deal_count": "Deal count" ,"roadmap": "Roadmap" ,"add_task": "Add task" ,"task_name": "Task name" ,"start_date": "Start date" ,"end_date": "End date" ,"status": "Status" ,"not_started": "Not started" ,"in_progress": "In progress" ,"completed": "Completed" ,"submit": "Submit" ,"timeline": "Timeline" ,"no_tasks": "No tasks defined. Use the form below to add tasks." ,"feature_catalog": "Feature Catalog" }, "ar": { "language": "اللغة", "welcome": "مرحبًا", "select_module": "اختر الوحدة", "dashboard": "لوحة القيادة", "kpi_analytics": "تحليلات الأداء", "advanced_analytics": "التحليلات المتقدمة", "proposal_generator": "مولد العروض", "portfolio_scorecard": "بطاقة محفظة المشاريع", "ai_copilot": "مساعد الذكاء الاصطناعي", "admin_panel": "لوحة الإدارة", "logout": "تسجيل الخروج", "upload_data": "حمّل بياناتك (CSV)", "no_data": "يرجى تحميل ملف CSV للبدء.", "total_records": "إجمالي السجلات", "average_value": "متوسط القيمة", "max_value": "أقصى قيمة", "advanced_modeling": "النمذجة باستخدام الغابة العشوائية", "select_target": "اختر عمود الهدف", "select_features": "اختر أعمدة الخصائص", "train_model": "تدريب النموذج", "model_results": "نتائج النموذج", "proposal_heading": "إنشاء عرض", "client_name": "اسم العميل", "project_scope": "نطاق المشروع", "generate_proposal": "إنشاء العرض", "proposal_output": "مخرجات العرض", "chat_with_ai": "تحدث مع الذكاء الاصطناعي عن بياناتك", "enter_question": "أدخل سؤالك", "send": "إرسال", "settings": "الإعدادات", "upload_success": "تم تحميل الملف بنجاح.", "sales_analytics": "تحليلات المبيعات وما قبل البيع", "select_sales_amount": "اختر عمود مبلغ المبيعات", "select_stage": "اختر عمود المرحلة", "select_outcome": "اختر عمود نتيجة الصفقة", "won_label": "التسمية للصفقات الرابحة", "funnel_title": "قمع المبيعات حسب المرحلة", "win_rate": "معدل الفوز", "sales_by_stage": "المبيعات حسب المرحلة", "sales_total": "إجمالي المبيعات", "average_deal_size": "متوسط حجم الصفقة", "won_deals": "الصفقات الرابحة", "lost_deals": "الصفقات الخاسرة", "deal_count": "عدد الصفقات" ,"roadmap": "خريطة الطريق" ,"add_task": "إضافة مهمة" ,"task_name": "اسم المهمة" ,"start_date": "تاريخ البدء" ,"end_date": "تاريخ الانتهاء" ,"status": "الحالة" ,"not_started": "لم تبدأ بعد" ,"in_progress": "قيد التنفيذ" ,"completed": "مكتملة" ,"submit": "إرسال" ,"timeline": "الجدول الزمني" ,"no_tasks": "لا توجد مهام. استخدم النموذج أدناه لإضافة المهام." ,"feature_catalog": "دليل الميزات" }, }
def t(key: str, lang: str) -> str: """Translate a UI string into the selected language.""" if lang not in TRANSLATIONS: lang = "en" return TRANSLATIONS.get(lang, {}).get(key, TRANSLATIONS["en"].get(key, key))
###############################################################################
Data handling
###############################################################################
@st.cache_data(show_spinner=False) def load_data(file) -> Optional[pd.DataFrame]: """Load data from a CSV uploaded by the user.""" if file is None: return None try: df = pd.read_csv(file)
Parse potential datetime columns
for col in df.columns: if df[col].dtype == object: try: df[col] = pd.to_datetime(df[col]) except (ValueError, TypeError): pass return df except Exception as e: st.error(f"Error reading file: {e}") return None
###############################################################################
Module implementations
###############################################################################
def show_dashboard(data: pd.DataFrame, lang: str) -> None: """Render the dashboard page.""" st.title(t("dashboard", lang)) if data is None: st.info(t("no_data", lang)) return
Identify numeric and datetime columns
numeric_cols = data.select_dtypes(include=[np.number]).columns date_cols = data.select_dtypes(include=["datetime64[ns]"]).columns if numeric_cols.empty: st.warning("No numeric columns found for summary statistics.") return if date_cols.empty: st.warning("No datetime columns found for time series chart.") return
Summary metrics on the first numeric column
y_col = numeric_cols[0] st.markdown(f"{t('total_records', lang)}: {len(data)}") st.markdown(f"{t('average_value', lang)} ({y_col}): {data[y_col].mean():.2f}") st.markdown(f"{t('max_value', lang)} ({y_col}): {data[y_col].max():.2f}")
with st.expander("Select columns for chart"): x_col = st.selectbox("Date column", date_cols, index=0, key="dashboard_date_col") y_col = st.selectbox("Value column", numeric_cols, index=0, key="dashboard_value_col")
import plotly.express as px fig = px.line( data.sort_values(x_col), x=x_col, y=y_col, title=f"{t('dashboard', lang)} – {y_col} vs {x_col}", labels={x_col: x_col, y_col: y_col}, ) st.plotly_chart(fig, use_container_width=True)
def show_kpi_analytics(data: pd.DataFrame, lang: str) -> None: """Render the KPI analytics module.""" st.title(t("kpi_analytics", lang)) if data is None: st.info(t("no_data", lang)) return
Identify potential KPI dimensions: categorical columns
categorical_cols = data.select_dtypes(include=["object", "category"]).columns numeric_cols = data.select_dtypes(include=[np.number]).columns if categorical_cols.empty or numeric_cols.empty: st.warning("Data must contain at least one categorical and one numeric column.") return
dimension = st.selectbox("Select dimension", categorical_cols, index=0) metric = st.selectbox("Select metric", numeric_cols, index=0)
grouped = data.groupby(dimension)[metric].agg(["count", "sum", "mean", "max", "min"]) grouped_sorted = grouped.sort_values("mean", ascending=False)
st.dataframe(grouped_sorted)
import plotly.express as px fig = px.bar( grouped_sorted.reset_index(), x=dimension, y="mean", title=f"{metric} mean by {dimension}", labels={dimension: dimension, "mean": f"Mean {metric}"}, ) st.plotly_chart(fig, use_container_width=True)
def show_advanced_analytics(data: pd.DataFrame, lang: str) -> None: """Render the advanced analytics module.""" st.title(t("advanced_analytics", lang)) if data is None: st.info(t("no_data", lang)) return if RandomForestRegressor is None: st.error("scikit‑learn is not installed. Please install scikit‑learn to use the advanced analytics module.") return
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist() if len(numeric_cols) < 2: st.warning("Dataset must contain at least two numeric columns for modeling.") return
model_type = st.radio("Model type", ["Regression", "Classification"], index=0) target = st.selectbox(t("select_target", lang), numeric_cols, index=0) feature_options = [col for col in numeric_cols if col != target] features = st.multiselect(t("select_features", lang), feature_options, default=feature_options) test_size = st.slider("Test size (%)", min_value=10, max_value=50, value=20, step=5)
if st.button(t("train_model", lang)): if model_type == "Regression": X = data[features] y = data[target] X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=test_size / 100.0, random_state=42 ) model = RandomForestRegressor(n_estimators=200, random_state=42) model.fit(X_train, y_train) y_pred = model.predict(X_test) rmse = mean_squared_error(y_test, y_pred, squared=False) r2 = r2_score(y_test, y_pred) st.subheader(t("model_results", lang)) st.write(f"RMSE: {rmse:.3f}") st.write(f"R²: {r2:.3f}") importances = model.feature_importances_ importance_df = pd.DataFrame({"feature": features, "importance": importances}).sort_values("importance", ascending=False) st.dataframe(importance_df) import plotly.express as px fig = px.bar(importance_df, x="feature", y="importance", title="Feature Importances", labels={"feature": "Feature", "importance": "Importance"}) st.plotly_chart(fig, use_container_width=True) else: # Classification if RandomForestClassifier is None: st.error("scikit‑learn is not installed. Please install scikit‑learn to use classification.") return
Convert target to categorical labels if necessary
y = data[target] if not pd.api.types.is_categorical_dtype(y) and y.dtype != object: st.error("Selected target column must contain categorical labels for classification.") return le = LabelEncoder() y_encoded = le.fit_transform(y.astype(str)) X = data[features] X_train, X_test, y_train, y_test = train_test_split( X, y_encoded, test_size=test_size / 100.0, random_state=42 ) clf = RandomForestClassifier(n_estimators=200, random_state=42) clf.fit(X_train, y_train) y_pred = clf.predict(X_test) acc = accuracy_score(y_test, y_pred) st.subheader(t("model_results", lang)) st.write(f"Accuracy: {acc:.3f}") importances = clf.feature_importances_ importance_df = pd.DataFrame({"feature": features, "importance": importances}).sort_values("importance", ascending=False) st.dataframe(importance_df) import plotly.express as px fig = px.bar(importance_df, x="feature", y="importance", title="Feature Importances", labels={"feature": "Feature", "importance": "Importance"}) st.plotly_chart(fig, use_container_width=True)
def generate_proposal_text(client_name: str, project_scope: str) -> str: """Generate a simple proposal text.""" return ( f"Dear {client_name},\n\n" f"Thank you for considering us for your project. We propose the following scope:\n" f"{project_scope}\n\n" f"Our team is committed to delivering high‑quality results using state‑of‑the‑art analytics and AI tools.\n\n" f"We look forward to working with you.\n\n" f"Best regards,\nYour Company" )
def show_proposal_generator(data: pd.DataFrame, lang: str) -> None: """Render the proposal generator module.""" st.title(t("proposal_generator", lang)) client_name = st.text_input(t("client_name", lang)) project_scope = st.text_area(t("project_scope", lang)) if st.button(t("generate_proposal", lang)): if not client_name or not project_scope: st.warning("Both client name and project scope are required.") else: proposal = generate_proposal_text(client_name, project_scope) st.subheader(t("proposal_output", lang)) st.code(proposal, language="markdown")
def show_portfolio_scorecard(data: pd.DataFrame, lang: str) -> None: """Render the portfolio scorecard module.""" st.title(t("portfolio_scorecard", lang)) if data is None: st.info(t("no_data", lang)) return cat_cols = data.select_dtypes(include=["object", "category"]).columns num_cols = data.select_dtypes(include=[np.number]).columns if cat_cols.empty or num_cols.empty: st.warning("Dataset must contain both categorical and numeric columns.") return category = st.selectbox("Category", cat_cols, index=0) metrics = st.multiselect("Metrics", num_cols, default=num_cols[:min(3, len(num_cols))]) scorecard = data.groupby(category)[metrics].mean().reset_index() st.dataframe(scorecard) import plotly.express as px fig = px.imshow( scorecard.set_index(category)[metrics], labels=dict(x="Metric", y=category, color="Value"), x=metrics, y=scorecard[category], aspect="auto", title="Portfolio Scorecard Heatmap", ) st.plotly_chart(fig, use_container_width=True)
def respond_to_question(question: str, data: pd.DataFrame) -> str: """Placeholder function for AI copilot responses.""" return ( "This is a placeholder response. Integrate an AI service here " "to provide meaningful answers based on your data." )
def show_ai_copilot(data: pd.DataFrame, lang: str) -> None: """Render the AI copilot module.""" st.title(t("ai_copilot", lang)) if data is None: st.info(t("no_data", lang)) return st.markdown(t("chat_with_ai", lang)) question = st.text_input(t("enter_question", lang)) if st.button(t("send", lang)): if not question: st.warning("Please enter a question.") else: response = respond_to_question(question, data) st.write(response)
def show_admin_panel(lang: str) -> None: """Render the admin panel.""" st.title(t("admin_panel", lang)) st.write("This section is reserved for administrative controls.") st.write("Implement user management, data source configuration and more here.")
def show_sales_analytics(data: pd.DataFrame, lang: str) -> None: """Render sales & pre‑sales analytics.
Provides key metrics and visualisations for sales pipelines. Users must specify which columns represent sales amounts, pipeline stage, and deal outcome (e.g. won/lost). The module computes win rates, aggregate sales by stage, and displays a funnel chart. """ st.title(t("sales_analytics", lang)) if data is None: st.info(t("no_data", lang)) return
Identify numeric and categorical columns
num_cols = data.select_dtypes(include=[np.number]).columns cat_cols = data.select_dtypes(include=["object", "category"]).columns if num_cols.empty or cat_cols.empty: st.warning("Dataset must contain numeric and categorical columns for sales analytics.") return amount_col = st.selectbox(t("select_sales_amount", lang), num_cols) stage_col = st.selectbox(t("select_stage", lang), cat_cols) outcome_col = st.selectbox(t("select_outcome", lang), cat_cols) won_value = st.text_input(t("won_label", lang), value="Won")
Compute metrics
total_sales = data[amount_col].sum() avg_deal = data[amount_col].mean() deal_count = len(data) won_deals = data[data[outcome_col] == won_value] win_rate = (len(won_deals) / deal_count) if deal_count > 0 else 0.0
Display metrics
col1, col2, col3, col4 = st.columns(4) col1.metric(t("sales_total", lang), f"{total_sales:,.2f}") col2.metric(t("average_deal_size", lang), f"{avg_deal:,.2f}") col3.metric(t("deal_count", lang), deal_count) col4.metric(t("win_rate", lang), f"{win_rate*100:.1f}%")
Aggregate sales by stage
by_stage = data.groupby(stage_col)[amount_col].agg(["count", "sum", "mean"]).reset_index() by_stage_sorted = by_stage.sort_values("sum", ascending=False) st.subheader(t("sales_by_stage", lang)) st.dataframe(by_stage_sorted) import plotly.express as px
Funnel chart: stage vs total sales sum
fig = px.funnel( by_stage_sorted, x="sum", y=stage_col, title=t("funnel_title", lang), labels={stage_col: stage_col, "sum": "Sales"}, ) st.plotly_chart(fig, use_container_width=True)
def show_roadmap(data: Optional[pd.DataFrame], lang: str) -> None: """Display and manage a business roadmap.
The roadmap is a required component of the application. It allows users to define tasks with start and end dates and a status. Tasks are stored in Streamlit session state. Optionally, if the uploaded dataset contains columns named 'task', 'start', 'end', and 'status', those will be displayed automatically as part of the roadmap. """ st.header(t("roadmap", lang))
Initialise session state for tasks if not already present
if "roadmap_tasks" not in st.session_state: st.session_state.roadmap_tasks = []
If the dataset contains roadmap columns, display them as initial tasks
if data is not None: if set(["task", "start", "end", "status"]).issubset(data.columns): df_tasks = data[["task", "start", "end", "status"]].dropna()
Merge loaded tasks with session state without duplicates
for _, row in df_tasks.iterrows(): task_dict = { "task": str(row["task"]), "start": pd.to_datetime(row["start"]).date(), "end": pd.to_datetime(row["end"]).date(), "status": str(row["status"]), } if task_dict not in st.session_state.roadmap_tasks: st.session_state.roadmap_tasks.append(task_dict)
Display existing tasks
if st.session_state.roadmap_tasks: roadmap_df = pd.DataFrame(st.session_state.roadmap_tasks) st.table(roadmap_df)
Display timeline with Plotly Gantt chart
import plotly.express as px fig = px.timeline( roadmap_df, x_start="start", x_end="end", y="task", color="status", title=t("timeline", lang), ) fig.update_yaxes(autorange="reversed") st.plotly_chart(fig, use_container_width=True) else: st.info(t("no_tasks", lang))
Task input form
with st.form(key="add_task_form", clear_on_submit=True): st.subheader(t("add_task", lang)) task_name = st.text_input(t("task_name", lang)) col1, col2 = st.columns(2) start_date = col1.date_input(t("start_date", lang)) end_date = col2.date_input(t("end_date", lang)) status = st.selectbox( t("status", lang), [t("not_started", lang), t("in_progress", lang), t("completed", lang)], ) submitted = st.form_submit_button(t("submit", lang)) if submitted: if not task_name: st.warning("Task name is required.") elif end_date < start_date: st.warning("End date cannot be before start date.") else: st.session_state.roadmap_tasks.append( { "task": task_name, "start": start_date, "end": end_date, "status": status, } ) st.success("Task added.")
def show_feature_catalog(lang: str) -> None: """Display the master feature catalog.
This page summarises the available modules, widgets, AI services, data processing tools, KPI components, and innovation roadmaps enumerated in the doganBS streamlit catalog. Use this as a reference for planning how to extend the app to support your transformation from reseller to master system integrator. """ st.title(t("feature_catalog", lang)) st.markdown( """ This catalog outlines a comprehensive suite of modules and technologies that can be integrated into your Strategic Intelligence Suite. The categories below list examples of Streamlit widgets, analytics components, data processing utilities, AI functions, KPIs, proposal tools, and innovative features. Use this guide to identify which components you need to support your business transformation. """ )
Category summaries
st.subheader("A. Core Streamlit UX Widgets") st.write( "Basic interactive elements such as buttons, file uploads, chat panes, " "progress indicators, notifications, toggles, dataframes, editable grids, " "metrics, sliders, pickers, date/time inputs, camera capture, and tabbed layouts. " "These widgets form the building blocks of your user interface." ) st.subheader("B. Advanced Streamlit Components") st.write( "Enhanced interface elements like sidebar option menus, Ag‑Grid tables, copy and keyboard shortcuts, " "keyword tagging, animations, third‑party report embedding, authentication, session state, and custom CSS." ) st.subheader("C. Plotly & Visual Analytics") st.write( "A wide variety of interactive charts including bar, line, scatter, treemap, sunburst, " "sankey, funnel, Gantt, heatmap, waterfall, gauges, violin plots, radar charts, 3‑D surfaces, and choropleths. " "Select the chart type that best represents your KPIs and operational metrics." ) st.subheader("D. Data Processing & Quality") st.write( "Libraries and techniques for cleaning and validating data: pandas pipelines, column standardisation, " "missing‑value visualisation, expectations frameworks, strict schema enforcement, in‑memory SQL via DuckDB, " "polars for large files, Parquet caching, parallel ETL with Dask, Excel/PDF extraction, fuzzy matching, " "date parsing, schema mapping, and error handling with logging." ) st.subheader("E. AI / LLM & Copilot Functions") st.write( "Integrations with OpenAI and other AI frameworks: natural‑language chat, retrieval‑augmented queries, vector stores, " "knowledge graphs, document QA, summarisation, sentiment classification, keyword extraction, text‑to‑speech and speech‑to‑text, " "function calling, time‑series forecasting, anomaly detection, reinforcement learning, and user preference learning." ) st.subheader("F. KPI & Executive Metrics") st.write( "Components for KPI management: dynamic KPI cards with thresholds, drill‑down filters, delta badges, snapshot comparators, " "weighted scorecards, idle cost trackers, compliance gauges, resource utilisation meters, and what‑if scenario simulators." ) st.subheader("G. RFQ / Proposal & Compliance") st.write( "Tools for managing RFQs and proposals: email inbox parsing, SharePoint integration, document templating, margin calculators, " "vendor clarification trackers, evaluation matrices, compliance checkers, form exporters, risk flagging, and PDF merging/stamping." ) st.subheader("H. Vendor / Technology Scoring") st.write( "Assess vendor capabilities through radar charts, vulnerability feeds, total cost calculators, readiness heatmaps, and lead‑time vs. SLA analysis." ) st.subheader("I. Business & Governance Utilities") st.write( "Role‑based authentication, audit ledgers, webhook badges, email exporters, and health‑check panels for external systems." ) st.subheader("J. Architecture (Front‑End / Back‑End / Data‑Layer") st.write( "Guidance on structuring your codebase: front‑end components live under /components/, back‑end logic and services live under /modules/, " "and persistent storage stays in the /data/ directory using DuckDB and Parquet." ) st.subheader("K. Predictive Mapping & Role‑Based Guidance") st.write( "Mappings that tailor the interface and predictive features to user roles (e.g., Solution Director, Sales Director, CEO). " "Each role is associated with specific screens and automation features such as win‑probability scoring, margin guardians, AI briefs, and smart assistants." ) st.subheader("L. Beyond‑Universe Innovations") st.write( "Experimental and forward‑looking capabilities such as quantum optimisers, drone synchronization, AR dashboards, blockchain audit ledgers, edge ML deployment, " "gesture navigation, cash‑flow simulators, ethical risk scanners, IoT heatmaps, emotion AI, and more." ) st.subheader("M. Global Pre‑Built Code & Role Mapping") st.write( "A library of ready‑to‑use Python modules supporting predictive cash flow, board‑pack generation, quantum optimisation, drone control, voice interfaces, auditing, " "edge deployment, gesture control, CO₂ estimation, sentiment analysis, FX hedging, weather overlay, infographics, CI/CD, self‑healing ETL, narrators, " "clause builders, crowd forecasting, decentralised login, zero‑copy data sharing, pricing bots, haptic alerts, org chart rendering, translation memory, " "cyber threat feeds, quantum‑safe encryption, floor plan mapping, budget burn gauges, automatic meeting minutes, stress‑responsive themes, offline caching, " "PDF sealing, multilingual OCR, drill‑path AI, explainable AI dashboards, retrieval‑augmented QA, cloud spend optimisation, KPI storyboarding, and more." )
###############################################################################
Main application
###############################################################################
def main() -> None: st.set_page_config(page_title="DoganLab Business Intelligence", layout="wide", initial_sidebar_state="expanded") lang = st.sidebar.selectbox("🌐 " + t("language", "en"), list(TRANSLATIONS.keys()), index=0) st.sidebar.markdown(f"### {t('upload_data', lang)}") uploaded_file = st.sidebar.file_uploader(label="", type=["csv"], accept_multiple_files=False) data = load_data(uploaded_file) if uploaded_file is not None and data is not None: st.sidebar.success(t("upload_success", lang))
Render roadmap (mandatory)
show_roadmap(data, lang)
Remaining modules (optional navigation)
st.sidebar.markdown(f"### {t('select_module', lang)}") modules = { t("dashboard", lang): show_dashboard, t("kpi_analytics", lang): show_kpi_analytics, t("advanced_analytics", lang): show_advanced_analytics, t("sales_analytics", lang): show_sales_analytics, t("proposal_generator", lang): show_proposal_generator, t("portfolio_scorecard", lang): show_portfolio_scorecard, t("ai_copilot", lang): show_ai_copilot, t("admin_panel", lang): show_admin_panel, t("feature_catalog", lang): show_feature_catalog, } module_names = list(modules.keys()) selected_module_name = st.sidebar.radio("", module_names, index=0) selected_module_fn = modules[selected_module_name]
Modules that only need the language argument (no data dependency)
single_arg_modules = [show_admin_panel, show_feature_catalog] if selected_module_fn in single_arg_modules: selected_module_fn(lang=lang) else: selected_module_fn(data=data, lang=lang) st.sidebar.button(t("logout", lang))
if name == "main": main()
any progress # doganlab_bi_app.py (Main Launcher)
# Streamlit-based Strategic Intelligence Suite — Fully Integrated with Live Data, AI-Driven Nudges, and Behavioral Alignment

try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("[ERROR] Streamlit is not installed. Please run: pip install streamlit")

from modules.ui_kpi_engine import show_kpi_engine
from modules.ui_ai_copilot import show_ai_copilot
from modules.ui_predictive_forecast import show_predictive_forecast
from modules.ui_proposal_builder import show_proposal_builder
from modules.ui_executive_dashboard import show_executive_dashboard
from modules.ui_action_panel import show_action_panel
from modules.ui_rfq_engine import show_rfq_engine
from modules.ui_vendor_scoring import show_vendor_scoring
from modules.ui_data_governance import show_data_governance
from modules.ui_market_command_center import show_market_command_center
from modules.ui_role_based_guidance import show_role_based_guidance
from modules.ui_org_alignment_bot import show_org_alignment_bot
from modules.ui_ai_insight_panel import show_ai_insight_panel

from modules.utils_alignment_status import (
    compute_alignment_status,
    trigger_behavioral_correction,
    compare_dept_behavior_vs_vision,
    issue_structured_alignment_alerts
)

alignment_status = compute_alignment_status()
trigger_behavioral_correction()
compare_dept_behavior_vs_vision()
issue_structured_alignment_alerts()

try:
    from modules.brain_market_telemetry import run_market_brain
    run_market_brain()
except Exception as e:
    print(f"[WARNING] Market telemetry module failed to load: {e}")

MODULES = {
    "🌟 Executive Dashboard": show_executive_dashboard,
    "📊 KPI Engine": show_kpi_engine,
    "🤖 AI Copilot": show_ai_copilot,
    "📈 Predictive Forecasting": show_predictive_forecast,
    "📄 Proposal Builder": show_proposal_builder,
    "🚦 Action Panel": show_action_panel,
    "📥 RFQ Engine": show_rfq_engine,
    "📡 Vendor Scoring": show_vendor_scoring,
    "📚 Data Governance": show_data_governance,
    "🧱 Market Command Center": show_market_command_center,
    "🎛️ AI Insight Panel": show_ai_insight_panel,
    "🪰 Role-Based Guidance": show_role_based_guidance,
    "📡 Org Alignment Bot": show_org_alignment_bot,
}

st.set_page_config(page_title="doganBS Strategic Suite", layout="wide")
st.sidebar.title("📌 Navigation")

display_modules = [f"{alignment_status.get(name, '⚪')} {name}" for name in MODULES.keys()]
selection_display = st.sidebar.radio("Select Module", display_modules)
selection = selection_display[2:] if len(selection_display) > 2 else selection_display

if selection in MODULES:
    MODULES[selection]()
else:
    st.error(f"Selected module '{selection}' is not recognized.")

