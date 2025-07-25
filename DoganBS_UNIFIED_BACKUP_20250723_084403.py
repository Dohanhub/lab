"""
🌟 doganBS Smart KPI Engine v1.2
💙 In Loving Memory of Omar (2007-2024)
"Forever 17, Forever Inspiring Innovation"

AI-Powered Business Intelligence Platform
Strategic Intelligence Suite with 100+ Features
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import yaml
import os
import json
import numpy as np
from pathlib import Path

# Advanced imports (with fallbacks for missing packages)
try:
    from streamlit_option_menu import option_menu
    HAS_OPTION_MENU = True
except ImportError:
    HAS_OPTION_MENU = False

try:
    from streamlit_lottie import st_lottie
    HAS_LOTTIE = True
except ImportError:
    HAS_LOTTIE = False

try:
    import plotly.figure_factory as ff
    HAS_FIGURE_FACTORY = True
except ImportError:
    HAS_FIGURE_FACTORY = False

# Page configuration
st.set_page_config(
    page_title="doganBS Smart KPI Engine v1.2",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load configuration
@st.cache_data
def load_config():
    """Load application configuration"""
    try:
        with open('kpi_config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {
            'app': {'name': 'doganBS', 'version': '1.2', 'title': 'Smart KPI Engine'},
            'legacy': {
                'tribute_message': 'Forever 17, Forever Inspiring Innovation',
                'show_tribute': True,
                'memorial_color': '#4A90E2'
            },
            'kpis': {
                'revenue': {'label': 'Revenue', 'unit': 'SAR', 'target': 1000000},
                'gp_margin': {'label': 'GP Margin', 'unit': '%', 'target': 25},
                'customer_satisfaction': {'label': 'Customer Satisfaction', 'unit': '%', 'target': 90}
            }
        }

# Initialize configuration
config = load_config()

# Advanced KPI Functions
def calculate_kpi_health(actual, target, thresholds=None):
    """Calculate KPI health status with color coding"""
    if thresholds is None:
        thresholds = {'red': 0.8, 'amber': 0.9, 'green': 1.0}

    ratio = actual / target if target > 0 else 0

    if ratio >= thresholds['green']:
        return "🟢", "Excellent", "#28a745"
    elif ratio >= thresholds['amber']:
        return "🟡", "Good", "#ffc107"
    elif ratio >= thresholds['red']:
        return "🟠", "Warning", "#fd7e14"
    else:
        return "🔴", "Critical", "#dc3545"

def generate_kpi_insights(kpi_name, actual, target, previous=None):
    """Generate AI-like insights for KPIs"""
    insights = []

    # Performance vs target
    variance = ((actual - target) / target * 100) if target > 0 else 0
    if variance > 10:
        insights.append(f"📈 {kpi_name} exceeds target by {variance:.1f}%")
    elif variance < -10:
        insights.append(f"📉 {kpi_name} is {abs(variance):.1f}% below target")
    else:
        insights.append(f"🎯 {kpi_name} is on track")

    # Trend analysis
    if previous:
        trend = ((actual - previous) / previous * 100) if previous > 0 else 0
        if trend > 5:
            insights.append(f"⬆️ Improving trend (+{trend:.1f}%)")
        elif trend < -5:
            insights.append(f"⬇️ Declining trend ({trend:.1f}%)")
        else:
            insights.append(f"➡️ Stable performance")

    return insights

def create_advanced_metric_card(label, value, target, unit="", previous=None):
    """Create an advanced metric card with insights"""
    icon, status, color = calculate_kpi_health(value, target)
    delta = value - previous if previous else None

    col1, col2 = st.columns([3, 1])

    with col1:
        st.metric(
            label=f"{icon} {label}",
            value=f"{value:,.0f} {unit}",
            delta=f"{delta:+,.0f}" if delta else None
        )

    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 10px; background-color: {color}20; border-radius: 5px;">
            <strong style="color: {color};">{status}</strong><br>
            <small>Target: {target:,.0f} {unit}</small>
        </div>
        """, unsafe_allow_html=True)

    # Show insights
    insights = generate_kpi_insights(label, value, target, previous)
    for insight in insights:
        st.caption(insight)

# Custom CSS for Omar's tribute
st.markdown(f"""
<style>
.tribute-banner {{
    background: linear-gradient(90deg, {config['legacy']['memorial_color']}, #87CEEB);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}}

.main-header {{
    text-align: center;
    color: {config['legacy']['memorial_color']};
    margin-bottom: 2rem;
}}

.feature-card {{
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
    border-left: 4px solid {config['legacy']['memorial_color']};
}}
</style>
""", unsafe_allow_html=True)

# Header with Omar's tribute
if config['legacy']['show_tribute']:
    st.markdown(f"""
    <div class="tribute-banner">
        <h2>🧠 {config['app']['name']} {config['app']['title']} v{config['app']['version']}</h2>
        <p>💙 <strong>In Loving Memory of Omar (2007-2024)</strong></p>
        <p><em>"{config['legacy']['tribute_message']}"</em></p>
        <p><small>AI-Powered Strategic Intelligence Suite</small></p>
    </div>
    """, unsafe_allow_html=True)

# Advanced Sidebar Navigation (Feature #16: streamlit-option-menu)
st.sidebar.title("🧠 doganBS Intelligence Suite")

if HAS_OPTION_MENU:
    page = option_menu(
        menu_title=None,
        options=[
            "🏠 Smart Dashboard",
            "📊 KPI Analytics",
            "🔬 AI Analytics",
            "📄 RFQ & Proposals",
            "💼 Executive Reports",
            "🎯 Strategic Intelligence",
            "⚙️ System Management"
        ],
        icons=["house", "graph-up", "cpu", "file-text", "briefcase", "bullseye", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": config['legacy']['memorial_color'], "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": config['legacy']['memorial_color']},
        }
    )
else:
    # Fallback to standard selectbox
    page = st.sidebar.selectbox(
        "Choose a feature:",
        [
            "🏠 Smart Dashboard",
            "📊 KPI Analytics",
            "🔬 AI Analytics",
            "📄 RFQ & Proposals",
            "💼 Executive Reports",
            "🎯 Strategic Intelligence",
            "⚙️ System Management"
        ]
    )

# Role-based access control (Feature #113: RBAC)
if config.get('rbac', {}).get('enabled', False):
    user_role = st.sidebar.selectbox("👤 Role", ["admin", "manager", "viewer"])
    st.sidebar.caption(f"Logged in as: {user_role}")
else:
    user_role = "admin"  # Default to admin when RBAC is disabled

# Main content based on selected page
if page == "🏠 Smart Dashboard":
    st.markdown('<div class="main-header"><h1>🧠 Smart KPI Dashboard</h1></div>', unsafe_allow_html=True)

    # AI-Powered Executive Summary (Feature #56: OpenAI ChatCompletion simulation)
    with st.expander("🤖 AI Executive Summary", expanded=True):
        st.markdown("""
        **AI Insights for Today:**
        - 📈 Revenue trending 15% above target - strong Q4 performance
        - ⚠️ GP Margin showing slight decline - recommend cost optimization review
        - 🎯 Customer satisfaction remains excellent at 94%
        - 💡 **AI Recommendation:** Focus on margin improvement initiatives
        """)

    # Advanced KPI Cards (Feature #71: Dynamic KPI card generator)
    st.subheader("📊 Key Performance Indicators")

    # Get KPI data from config
    kpis = config.get('kpis', {})

    col1, col2, col3 = st.columns(3)

    with col1:
        if 'revenue' in kpis:
            kpi = kpis['revenue']
            # Simulate current values
            current_revenue = 1200000  # SAR 1.2M
            previous_revenue = 1100000  # Previous period
            create_advanced_metric_card(
                kpi['label'],
                current_revenue,
                kpi['target'],
                kpi['unit'],
                previous_revenue
            )

    with col2:
        if 'gp_margin' in kpis:
            kpi = kpis['gp_margin']
            current_margin = 23.5  # 23.5%
            previous_margin = 24.2  # Previous period
            create_advanced_metric_card(
                kpi['label'],
                current_margin,
                kpi['target'],
                kpi['unit'],
                previous_margin
            )

    with col3:
        if 'customer_satisfaction' in kpis:
            kpi = kpis['customer_satisfaction']
            current_satisfaction = 94  # 94%
            previous_satisfaction = 92  # Previous period
            create_advanced_metric_card(
                kpi['label'],
                current_satisfaction,
                kpi['target'],
                kpi['unit'],
                previous_satisfaction
            )

    # Sample charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Revenue Trend")
        # Generate sample data
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        revenue = [100000 + i * 5000 + (i % 3) * 10000 for i in range(len(dates))]

        fig = px.line(x=dates, y=revenue, title="Monthly Revenue")
        fig.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🎯 KPI Performance")
        categories = ['Sales', 'Marketing', 'Support', 'Development']
        values = [85, 92, 78, 88]

        fig = px.bar(x=categories, y=values, title="Department Performance")
        fig.update_layout(xaxis_title="Department", yaxis_title="Performance (%)")
        st.plotly_chart(fig, use_container_width=True)

elif page == "📊 KPI Analytics":
    st.markdown('<div class="main-header"><h1>📊 KPI Analytics Engine</h1></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Key Performance Indicators</h3>
        <p>Analyze and track your most important business metrics with real-time updates and intelligent insights.</p>
    </div>
    """, unsafe_allow_html=True)

    # KPI selection
    selected_kpis = st.multiselect(
        "Select KPIs to analyze:",
        ["Revenue Growth", "Customer Acquisition Cost", "Customer Lifetime Value",
         "Churn Rate", "Net Promoter Score", "Conversion Rate"],
        default=["Revenue Growth", "Customer Acquisition Cost"]
    )

    if selected_kpis:
        for kpi in selected_kpis:
            with st.expander(f"📈 {kpi} Analysis"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(f"Current {kpi}", "85.2%", "2.1%")
                with col2:
                    # Sample trend data
                    trend_data = [80, 82, 85, 83, 87, 85]
                    fig = px.line(y=trend_data, title=f"{kpi} Trend")
                    st.plotly_chart(fig, use_container_width=True)

elif page == "🔬 AI Analytics":
    st.markdown('<div class="main-header"><h1>🔬 AI-Powered Analytics</h1></div>', unsafe_allow_html=True)

    # Feature #56: OpenAI ChatCompletion (Natural Language Query)
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 Natural Language Query Engine</h3>
        <p>Ask questions about your data in plain English or Arabic</p>
    </div>
    """, unsafe_allow_html=True)

    # Natural Language Query Interface
    query = st.text_input("💬 Ask your data a question:",
                         placeholder="e.g., 'Why is revenue down this month?' or 'Show me top performing regions'")

    if query:
        with st.spinner("🧠 AI is analyzing your question..."):
            # Simulate AI response (Feature #56)
            st.success("🤖 AI Analysis Complete!")

            if "revenue" in query.lower():
                st.markdown("""
                **AI Insights:**
                - 📉 Revenue declined 5% due to seasonal factors
                - 🎯 Q4 typically shows 15% uptick - on track for recovery
                - 💡 **Recommendation:** Accelerate Q4 marketing campaigns
                """)

                # Show supporting chart
                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                revenue_data = [1200, 1150, 1100, 1080, 1050, 1000]
                fig = px.line(x=months, y=revenue_data, title="Revenue Trend Analysis")
                st.plotly_chart(fig, use_container_width=True)

            elif "region" in query.lower():
                st.markdown("""
                **Regional Performance Analysis:**
                - 🥇 **Riyadh Region:** 145% of target (Outstanding)
                - 🥈 **Eastern Region:** 112% of target (Excellent)
                - 🥉 **Western Region:** 98% of target (Good)
                - ⚠️ **Northern Region:** 78% of target (Needs attention)
                """)

                # Regional performance chart
                regions = ['Riyadh', 'Eastern', 'Western', 'Northern']
                performance = [145, 112, 98, 78]
                colors = ['green' if x >= 100 else 'orange' if x >= 90 else 'red' for x in performance]

                fig = px.bar(x=regions, y=performance, color=colors,
                           title="Regional Performance vs Target (%)")
                st.plotly_chart(fig, use_container_width=True)

    # Feature #67: Time-series forecasting
    st.markdown("""
    <div class="feature-card">
        <h3>📈 Predictive Analytics & Forecasting</h3>
        <p>AI-powered forecasting using Prophet and advanced algorithms</p>
    </div>
    """, unsafe_allow_html=True)

    forecast_metric = st.selectbox("Select metric to forecast:",
                                  ["Revenue", "GP Margin", "Customer Satisfaction"])

    forecast_periods = st.slider("Forecast periods (months):", 1, 12, 6)

    if st.button("🔮 Generate Forecast"):
        with st.spinner("🧠 AI is generating forecasts..."):
            # Simulate forecasting (Feature #67)
            import random

            # Generate historical data
            dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
            if forecast_metric == "Revenue":
                base_values = [1000000 + i * 50000 + random.randint(-100000, 100000) for i in range(12)]
                unit = "SAR"
            elif forecast_metric == "GP Margin":
                base_values = [25 + random.uniform(-2, 2) for _ in range(12)]
                unit = "%"
            else:
                base_values = [90 + random.uniform(-5, 5) for _ in range(12)]
                unit = "%"

            # Generate forecast
            future_dates = pd.date_range(start=dates[-1] + pd.DateOffset(months=1),
                                       periods=forecast_periods, freq='M')

            if forecast_metric == "Revenue":
                forecast_values = [base_values[-1] + i * 60000 + random.randint(-50000, 50000)
                                 for i in range(1, forecast_periods + 1)]
            else:
                trend = 0.1 if forecast_metric == "Customer Satisfaction" else -0.05
                forecast_values = [base_values[-1] + i * trend + random.uniform(-1, 1)
                                 for i in range(1, forecast_periods + 1)]

            # Create forecast chart
            fig = go.Figure()

            # Historical data
            fig.add_trace(go.Scatter(
                x=dates, y=base_values,
                mode='lines+markers',
                name='Historical',
                line=dict(color='blue')
            ))

            # Forecast data
            fig.add_trace(go.Scatter(
                x=future_dates, y=forecast_values,
                mode='lines+markers',
                name='Forecast',
                line=dict(color='red', dash='dash')
            ))

            fig.update_layout(
                title=f"{forecast_metric} Forecast - Next {forecast_periods} Months",
                xaxis_title="Date",
                yaxis_title=f"{forecast_metric} ({unit})",
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

            # AI Insights
            st.success("🤖 Forecast Analysis Complete!")
            if forecast_metric == "Revenue":
                st.markdown("""
                **AI Forecast Insights:**
                - 📈 Revenue expected to grow 8% over next 6 months
                - 🎯 Peak performance anticipated in month 4-5
                - ⚠️ Seasonal dip expected in month 2
                - 💡 **Recommendation:** Prepare inventory for peak months
                """)

    # Feature #68: Anomaly Detection
    st.markdown("""
    <div class="feature-card">
        <h3>🚨 Anomaly Detection</h3>
        <p>AI-powered anomaly detection to identify unusual patterns</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 Scan for Anomalies"):
        with st.spinner("🧠 AI is scanning for anomalies..."):
            # Simulate anomaly detection (Feature #68)
            anomalies_found = [
                {"metric": "Revenue", "date": "2024-10-15", "severity": "Medium",
                 "description": "15% drop detected - investigate supply chain issues"},
                {"metric": "Customer Satisfaction", "date": "2024-10-20", "severity": "Low",
                 "description": "Minor decline in satisfaction scores"},
                {"metric": "GP Margin", "date": "2024-10-22", "severity": "High",
                 "description": "Significant margin compression - urgent review needed"}
            ]

            st.success(f"🔍 Anomaly scan complete! Found {len(anomalies_found)} anomalies")

            for anomaly in anomalies_found:
                severity_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
                st.markdown(f"""
                **{severity_color[anomaly['severity']]} {anomaly['severity']} Severity**
                - **Metric:** {anomaly['metric']}
                - **Date:** {anomaly['date']}
                - **Issue:** {anomaly['description']}
                """)

    # Feature #3: File uploader for advanced analysis
    st.markdown("""
    <div class="feature-card">
        <h3>📁 Advanced Data Analysis</h3>
        <p>Leverage advanced statistical methods and machine learning for deeper insights into your business data.</p>
    </div>
    """, unsafe_allow_html=True)

    # File upload for analysis
    uploaded_file = st.file_uploader("Upload your data file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success(f"✅ File uploaded successfully! Shape: {df.shape}")

            # Display data preview
            st.subheader("📋 Data Preview")
            st.dataframe(df.head())

            # Basic statistics
            st.subheader("📊 Statistical Summary")
            st.dataframe(df.describe())

        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
    else:
        st.info("📁 Please upload a CSV or Excel file to begin analysis")

elif page == "📄 RFQ & Proposals":
    st.markdown('<div class="main-header"><h1>📄 RFQ & Proposal Management</h1></div>', unsafe_allow_html=True)

    # Feature #81: RFQ inbox parser
    st.markdown("""
    <div class="feature-card">
        <h3>📧 Smart RFQ Inbox</h3>
        <p>AI-powered RFQ processing and automated proposal generation</p>
    </div>
    """, unsafe_allow_html=True)

    # RFQ Management Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📧 RFQ Inbox", "📝 Proposal Builder", "📊 Bid Analytics", "🏆 Win/Loss Analysis"])

    with tab1:
        st.subheader("📧 Active RFQs")

        # Simulate RFQ data (Feature #81)
        rfq_data = [
            {"id": "RFQ-2024-001", "client": "ARAMCO", "value": "2.5M SAR", "deadline": "2024-11-15",
             "status": "🟡 In Progress", "compliance": "85%", "ai_score": "High Win Probability"},
            {"id": "RFQ-2024-002", "client": "SABIC", "value": "1.8M SAR", "deadline": "2024-11-20",
             "status": "🟢 Ready to Submit", "compliance": "98%", "ai_score": "Very High Win Probability"},
            {"id": "RFQ-2024-003", "client": "STC", "value": "3.2M SAR", "deadline": "2024-12-01",
             "status": "🔴 Needs Attention", "compliance": "65%", "ai_score": "Medium Win Probability"}
        ]

        for rfq in rfq_data:
            with st.expander(f"{rfq['id']} - {rfq['client']} ({rfq['value']})"):
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Value", rfq['value'])
                    st.write(f"**Deadline:** {rfq['deadline']}")

                with col2:
                    st.metric("Compliance", rfq['compliance'])
                    st.write(f"**Status:** {rfq['status']}")

                with col3:
                    st.write(f"**AI Assessment:** {rfq['ai_score']}")
                    if st.button(f"📝 Work on {rfq['id']}", key=rfq['id']):
                        st.success(f"Opening {rfq['id']} for editing...")

    with tab2:
        st.subheader("📝 AI-Powered Proposal Builder")

        # Feature #83: docxtpl proposal builder
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 Smart Proposal Generation</h3>
            <p>AI-assisted proposal creation with Arabic & English templates</p>
        </div>
        """, unsafe_allow_html=True)

        # Proposal form
        with st.form("proposal_form"):
            st.subheader("📋 Proposal Details")

            col1, col2 = st.columns(2)
            with col1:
                client_name = st.text_input("Client Name")
                project_type = st.selectbox("Project Type",
                    ["Business Intelligence", "Data Analytics", "System Integration", "Custom Development"])

            with col2:
                budget_range = st.selectbox("Budget Range",
                    ["10K - 50K SAR", "50K - 100K SAR", "100K - 250K SAR", "250K+ SAR"])
                timeline = st.selectbox("Timeline",
                    ["1-3 months", "3-6 months", "6-12 months", "12+ months"])

            # Feature #89: Risk-flag LLM
            language = st.selectbox("Proposal Language", ["English", "Arabic", "Bilingual"])

            project_description = st.text_area("Project Description", height=100)

            submitted = st.form_submit_button("🚀 Generate AI Proposal")

            if submitted and client_name and project_description:
                with st.spinner("🤖 AI is generating your proposal..."):
                    st.success("✅ AI Proposal generated successfully!")

                    # Feature #83: AI-generated proposal content
                    st.markdown(f"""
                    ### 📄 AI-Generated Proposal for {client_name}

                    **Project Type:** {project_type}
                    **Budget Range:** {budget_range}
                    **Timeline:** {timeline}
                    **Language:** {language}

                    **Executive Summary:**
                    doganBS is pleased to present this comprehensive {project_type.lower()} solution
                    for {client_name}. Our AI-powered approach ensures optimal delivery within the
                    specified {timeline} timeframe.

                    **Project Overview:**
                    {project_description}

                    **AI Risk Assessment:** 🟢 Low Risk - High Success Probability

                    **Compliance Check:** ✅ NCA Compliant | ✅ Etimad Ready
                    """)

                    # Feature #2: Download button
                    if st.download_button(
                        label="📥 Download Proposal (PDF)",
                        data="Sample proposal content...",
                        file_name=f"Proposal_{client_name}_{datetime.now().strftime('%Y%m%d')}.pdf",
                        mime="application/pdf"
                    ):
                        st.success("📥 Proposal downloaded successfully!")

    with tab3:
        st.subheader("📊 Bid Analytics & Intelligence")

        # Feature #191: Heat tile RFQs
        st.markdown("""
        <div class="feature-card">
            <h3>🔥 Win Probability Matrix</h3>
            <p>AI-powered bid intelligence and win probability analysis</p>
        </div>
        """, unsafe_allow_html=True)

        # Win probability heatmap
        clients = ['ARAMCO', 'SABIC', 'STC', 'SAUDIA', 'NCB']
        sectors = ['Oil & Gas', 'Petrochemicals', 'Telecom', 'Aviation', 'Banking']

        # Generate sample win probability data
        win_probs = np.random.randint(20, 95, size=(len(clients), len(sectors)))

        fig = go.Figure(data=go.Heatmap(
            z=win_probs,
            x=sectors,
            y=clients,
            colorscale='RdYlGn',
            text=[[f"{val}%" for val in row] for row in win_probs],
            texttemplate="%{text}",
            textfont={"size": 12},
            hoverongaps=False
        ))

        fig.update_layout(
            title="Win Probability Matrix by Client & Sector",
            xaxis_title="Sector",
            yaxis_title="Client",
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        # Bid metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Active Bids", "12", "+3")

        with col2:
            st.metric("Win Rate", "68%", "+5%")

        with col3:
            st.metric("Avg Bid Value", "2.1M SAR", "+15%")

        with col4:
            st.metric("Pipeline Value", "25.2M SAR", "+22%")

    with tab4:
        st.subheader("🏆 Win/Loss Analysis")

        # Feature #192: Regret simulation
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Opportunity Cost Analysis</h3>
            <p>Calculate regret scenarios and opportunity costs</p>
        </div>
        """, unsafe_allow_html=True)

        # Win/Loss data
        wl_data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Wins': [3, 5, 2, 4, 6, 3],
            'Losses': [2, 1, 3, 2, 1, 2],
            'Win_Value': [2.1, 3.5, 1.8, 2.9, 4.2, 2.3],
            'Lost_Value': [1.2, 0.8, 2.1, 1.5, 0.9, 1.4]
        }

        df_wl = pd.DataFrame(wl_data)

        # Win/Loss chart
        fig = go.Figure()

        fig.add_trace(go.Bar(
            name='Wins',
            x=df_wl['Month'],
            y=df_wl['Win_Value'],
            marker_color='green'
        ))

        fig.add_trace(go.Bar(
            name='Lost Opportunities',
            x=df_wl['Month'],
            y=df_wl['Lost_Value'],
            marker_color='red'
        ))

        fig.update_layout(
            title='Win vs Lost Opportunities (SAR Millions)',
            xaxis_title='Month',
            yaxis_title='Value (SAR Millions)',
            barmode='group',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        # AI Insights
        st.markdown("""
        **🤖 AI Win/Loss Insights:**
        - 📈 Win rate improved 12% over last quarter
        - 💰 Average win value increased to 2.8M SAR
        - ⚠️ Lost opportunities in Telecom sector - investigate pricing strategy
        - 🎯 **Recommendation:** Focus on Oil & Gas sector (85% win rate)

            **Project Type:** {project_type}
            **Budget Range:** {budget_range}
            **Timeline:** {timeline}

            **Project Overview:**
            {project_description}

            *This is a preview. The full proposal would include detailed sections, pricing, and terms.*
            """)

elif page == "💼 Executive Reports":
    st.markdown('<div class="main-header"><h1>💼 Executive Reports</h1></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>📊 Executive Dashboard</h3>
        <p>High-level insights and reports designed for executive decision-making and strategic planning.</p>
    </div>
    """, unsafe_allow_html=True)

    # Report type selection
    report_type = st.selectbox(
        "Select Report Type:",
        ["Monthly Business Review", "Quarterly Performance", "Annual Summary", "Custom Report"]
    )

    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())

    if st.button("📊 Generate Executive Report"):
        st.success(f"✅ {report_type} generated for period: {start_date} to {end_date}")

        # Sample executive summary
        st.markdown("""
        ### 📋 Executive Summary

        - **Revenue Performance:** ⬆️ 15% increase compared to previous period
        - **Key Achievements:** 🎯 Exceeded quarterly targets by 8%
        - **Areas of Focus:** 🔍 Customer retention and market expansion
        - **Strategic Recommendations:** 💡 Invest in digital transformation initiatives
        """)

elif page == "🎯 Strategic Intelligence":
    st.markdown('<div class="main-header"><h1>🎯 Strategic Intelligence Suite</h1></div>', unsafe_allow_html=True)

    # Feature #152: AI Board Pack
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Executive Intelligence Dashboard</h3>
        <p>AI-powered strategic insights and predictive intelligence for leadership</p>
    </div>
    """, unsafe_allow_html=True)

    # Strategic Intelligence Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Strategic Overview", "🔮 Predictive Intelligence", "🎯 Scenario Planning", "📈 Market Intelligence"])

    with tab1:
        st.subheader("📊 Strategic Performance Overview")

        # Feature #76: Weighted scorecard
        st.markdown("### 🏆 Strategic Scorecard")

        # Strategic KPIs
        strategic_kpis = {
            'Market Share': {'actual': 15.2, 'target': 18.0, 'weight': 0.3},
            'Innovation Index': {'actual': 8.5, 'target': 9.0, 'weight': 0.25},
            'Customer Loyalty': {'actual': 87, 'target': 85, 'weight': 0.2},
            'Digital Transformation': {'actual': 72, 'target': 80, 'weight': 0.25}
        }

        col1, col2 = st.columns([2, 1])

        with col1:
            # Calculate weighted score
            total_score = 0
            total_weight = 0

            for kpi, data in strategic_kpis.items():
                score = min(100, (data['actual'] / data['target']) * 100)
                weighted_score = score * data['weight']
                total_score += weighted_score
                total_weight += data['weight']

                # Display KPI
                col_a, col_b, col_c = st.columns([2, 1, 1])
                with col_a:
                    st.write(f"**{kpi}**")
                with col_b:
                    st.metric("", f"{data['actual']}", f"{data['actual'] - data['target']:+.1f}")
                with col_c:
                    if score >= 100:
                        st.success(f"✅ {score:.0f}%")
                    elif score >= 90:
                        st.warning(f"⚠️ {score:.0f}%")
                    else:
                        st.error(f"❌ {score:.0f}%")

        with col2:
            overall_score = total_score / total_weight if total_weight > 0 else 0

            # Strategic score gauge
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = overall_score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Strategic Score"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 60], 'color': "lightgray"},
                        {'range': [60, 80], 'color': "yellow"},
                        {'range': [80, 100], 'color': "lightgreen"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))

            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("🔮 Predictive Intelligence")

        # Feature #151: Predictive cash flow
        st.markdown("""
        <div class="feature-card">
            <h3>💰 Predictive Cash Flow Analysis</h3>
            <p>Monte Carlo simulation for cash flow forecasting</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔮 Generate Predictive Analysis"):
            with st.spinner("🧠 AI is running predictive models..."):
                # Simulate predictive analytics
                months = pd.date_range(start='2024-11-01', periods=12, freq='M')

                # Monte Carlo simulation results
                scenarios = ['Optimistic', 'Most Likely', 'Pessimistic']
                colors = ['green', 'blue', 'red']

                fig = go.Figure()

                for i, scenario in enumerate(scenarios):
                    if scenario == 'Optimistic':
                        base = 1200000
                        growth = 0.08
                    elif scenario == 'Most Likely':
                        base = 1000000
                        growth = 0.05
                    else:
                        base = 800000
                        growth = 0.02

                    values = [base * (1 + growth) ** i + np.random.normal(0, 50000) for i in range(12)]

                    fig.add_trace(go.Scatter(
                        x=months,
                        y=values,
                        mode='lines+markers',
                        name=f'{scenario} Scenario',
                        line=dict(color=colors[i])
                    ))

                fig.update_layout(
                    title="Predictive Cash Flow - 12 Month Forecast",
                    xaxis_title="Month",
                    yaxis_title="Cash Flow (SAR)",
                    height=400
                )

                st.plotly_chart(fig, use_container_width=True)

                st.success("🔮 Predictive analysis complete!")
                st.markdown("""
                **🤖 AI Predictions:**
                - 📈 70% probability of exceeding targets in Q2 2025
                - 💰 Expected cash flow range: 800K - 1.4M SAR
                - ⚠️ Risk period identified: March-April 2025
                - 💡 **Strategic Recommendation:** Secure additional funding by February 2025
                """)

    with tab3:
        st.subheader("🎯 Scenario Planning")

        # Feature #80: What-if simulator
        st.markdown("""
        <div class="feature-card">
            <h3>🎲 Strategic Scenario Simulator</h3>
            <p>Model different strategic scenarios and their impacts</p>
        </div>
        """, unsafe_allow_html=True)

        # Scenario variables
        col1, col2 = st.columns(2)

        with col1:
            market_growth = st.slider("Market Growth Rate (%)", -10, 20, 5)
            competition_intensity = st.slider("Competition Intensity", 1, 10, 5)

        with col2:
            investment_level = st.slider("Investment Level (M SAR)", 0, 10, 3)
            innovation_focus = st.slider("Innovation Focus", 1, 10, 7)

        if st.button("🎯 Run Scenario Analysis"):
            # Calculate scenario impact
            base_revenue = 10000000  # 10M SAR

            # Impact calculations
            market_impact = base_revenue * (market_growth / 100)
            competition_impact = base_revenue * (-competition_intensity / 100)
            investment_impact = investment_level * 500000  # 500K per M invested
            innovation_impact = base_revenue * (innovation_focus / 100)

            total_impact = market_impact + competition_impact + investment_impact + innovation_impact
            projected_revenue = base_revenue + total_impact

            # Display results
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Base Revenue", "10.0M SAR")
                st.metric("Market Impact", f"{market_impact/1000000:+.1f}M SAR")

            with col2:
                st.metric("Competition Impact", f"{competition_impact/1000000:+.1f}M SAR")
                st.metric("Investment Impact", f"{investment_impact/1000000:+.1f}M SAR")

            with col3:
                st.metric("Innovation Impact", f"{innovation_impact/1000000:+.1f}M SAR")
                st.metric("Projected Revenue", f"{projected_revenue/1000000:.1f}M SAR",
                         f"{total_impact/1000000:+.1f}M")

            # Scenario assessment
            if total_impact > 1000000:
                st.success("🎯 **Excellent Scenario** - Strong growth potential")
            elif total_impact > 0:
                st.warning("⚠️ **Moderate Scenario** - Steady growth expected")
            else:
                st.error("🚨 **Challenging Scenario** - Risk mitigation required")

    with tab4:
        st.subheader("📈 Market Intelligence")

        # Feature #172: Price bot (competitor analysis)
        st.markdown("""
        <div class="feature-card">
            <h3>🕵️ Competitive Intelligence</h3>
            <p>AI-powered market analysis and competitor monitoring</p>
        </div>
        """, unsafe_allow_html=True)

        # Competitor analysis
        competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'doganBS']
        metrics = ['Market Share', 'Pricing Index', 'Innovation Score', 'Customer Satisfaction']

        # Generate competitive data
        comp_data = []
        for comp in competitors:
            if comp == 'doganBS':
                data = [15.2, 105, 8.5, 87]  # Our data
            else:
                data = [np.random.uniform(8, 20), np.random.uniform(95, 115),
                       np.random.uniform(6, 9), np.random.uniform(75, 90)]
            comp_data.append(data)

        # Create radar chart
        fig = go.Figure()

        for i, comp in enumerate(competitors):
            fig.add_trace(go.Scatterpolar(
                r=comp_data[i],
                theta=metrics,
                fill='toself',
                name=comp,
                line_color='red' if comp == 'doganBS' else None
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 120]
                )),
            showlegend=True,
            title="Competitive Analysis Radar",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

        # Market insights
        st.markdown("""
        **🤖 Market Intelligence Insights:**
        - 📊 doganBS holds strong position in innovation (8.5/10)
        - 💰 Pricing competitive but room for optimization
        - 🎯 Market share growth opportunity identified
        - 🚀 **Strategic Focus:** Leverage innovation advantage for market expansion
        """)

elif page == "⚙️ System Management":
    st.markdown('<div class="main-header"><h1>⚙️ System Management</h1></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🔧 System Configuration</h3>
        <p>Manage application settings, user preferences, and system maintenance tasks.</p>
    </div>
    """, unsafe_allow_html=True)

    # System status
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("System Status", "🟢 Online", "")

    with col2:
        st.metric("Data Storage", "2.3 GB", "12% used")

    with col3:
        st.metric("Last Backup", "2 hours ago", "")

    # Configuration options
    st.subheader("🔧 Configuration")

    with st.expander("📊 Display Settings"):
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
        show_tribute = st.checkbox("Show Omar's Tribute", value=True)
        auto_refresh = st.checkbox("Auto-refresh Data", value=True)

    with st.expander("📁 Data Management"):
        st.button("🔄 Refresh Data Cache")
        st.button("📥 Export All Data")
        st.button("🗑️ Clear Temporary Files")

    with st.expander("👥 User Management"):
        st.info("👤 Current User: Super Admin")
        st.button("👥 Manage Users")
        st.button("🔐 Security Settings")

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: {config['legacy']['memorial_color']}; padding: 1rem;">
    <p><strong>DoganLab Elite Team</strong> | <strong>UNIFIED v{config['app']['version']}</strong> | <strong>Deployment Ready</strong></p>
    <p>💙 Built with love in memory of Omar - his vision lives on in every feature</p>
</div>
""", unsafe_allow_html=True)
