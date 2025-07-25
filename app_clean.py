
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()"""
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()"""
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()"""
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()"""
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()"""
🚀 ABDULLAH FOUAD COMPANY - KPI DASHBOARD 🚀
===========================================

Advanced KPI Dashboard with Interactive Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
from datetime import datetime, timedelta
import json
import os
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="🚀 ABDULLAH FOUAD - KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Load sample KPI data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    data = {
        'Date': dates,
        'Sales': np.random.normal(100000, 20000, len(dates)).cumsum(),
        'Pre_Sales': np.random.normal(50000, 10000, len(dates)).cumsum(),
        'Sector_Performance': np.random.normal(75000, 15000, len(dates)).cumsum(),
        'Pipeline': np.random.normal(200000, 40000, len(dates)).cumsum(),
        'Team': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D'], len(dates)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

def create_kpi_cards(df):
    """Create KPI metric cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    current_sales = df['Sales'].iloc[-1]
    prev_sales = df['Sales'].iloc[-30] if len(df) > 30 else df['Sales'].iloc[0]
    sales_change = ((current_sales - prev_sales) / prev_sales) * 100
    
    current_presales = df['Pre_Sales'].iloc[-1]
    prev_presales = df['Pre_Sales'].iloc[-30] if len(df) > 30 else df['Pre_Sales'].iloc[0]
    presales_change = ((current_presales - prev_presales) / prev_presales) * 100
    
    current_sector = df['Sector_Performance'].iloc[-1]
    prev_sector = df['Sector_Performance'].iloc[-30] if len(df) > 30 else df['Sector_Performance'].iloc[0]
    sector_change = ((current_sector - prev_sector) / prev_sector) * 100
    
    current_pipeline = df['Pipeline'].iloc[-1]
    prev_pipeline = df['Pipeline'].iloc[-30] if len(df) > 30 else df['Pipeline'].iloc[0]
    pipeline_change = ((current_pipeline - prev_pipeline) / prev_pipeline) * 100
    
    with col1:
        st.metric(
            label="💰 Sales",
            value=f"${current_sales:,.0f}",
            delta=f"{sales_change:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="🎯 Pre-Sales",
            value=f"${current_presales:,.0f}",
            delta=f"{presales_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            label="🏢 Sector Performance",
            value=f"${current_sector:,.0f}",
            delta=f"{sector_change:+.1f}%"
        )
    
    with col4:
        st.metric(
            label="📈 Pipeline",
            value=f"${current_pipeline:,.0f}",
            delta=f"{pipeline_change:+.1f}%"
        )

def create_trend_charts(df):
    """Create trend analysis charts"""
    
    # Monthly aggregation
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    # Main trend chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#667eea', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pre_Sales'],
        mode='lines+markers',
        name='Pre-Sales',
        line=dict(color='#764ba2', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Sector_Performance'],
        mode='lines+markers',
        name='Sector Performance',
        line=dict(color='#f093fb', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Pipeline'],
        mode='lines+markers',
        name='Pipeline',
        line=dict(color='#f5576c', width=3)
    ))
    
    fig.update_layout(
        title="📊 KPI Trends Over Time",
        xaxis_title="Month",
        yaxis_title="Value ($)",
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_team_performance(df):
    """Create team performance analysis"""
    team_data = df.groupby('Team').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.bar(
        team_data,
        x='Team',
        y=['Sales', 'Pre_Sales', 'Sector_Performance', 'Pipeline'],
        title="👥 Team Performance Comparison",
        template='plotly_dark',
        height=400
    )
    
    return fig

def create_regional_analysis(df):
    """Create regional performance analysis"""
    regional_data = df.groupby('Region').agg({
        'Sales': 'sum',
        'Pre_Sales': 'sum',
        'Sector_Performance': 'sum',
        'Pipeline': 'sum'
    }).reset_index()
    
    fig = px.pie(
        regional_data,
        values='Sales',
        names='Region',
        title="🌍 Regional Sales Distribution",
        template='plotly_dark',
        height=400
    )
    
    return fig

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 ABDULLAH FOUAD COMPANY</h1>
        <h2>📊 Advanced KPI Dashboard</h2>
        <p>Real-time Business Intelligence & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Dashboard Controls")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Team filter
    selected_teams = st.sidebar.multiselect(
        "Select Teams",
        options=df['Team'].unique(),
        default=df['Team'].unique()
    )
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    df_filtered = df_filtered[df_filtered['Team'].isin(selected_teams)]
    df_filtered = df_filtered[df_filtered['Region'].isin(selected_regions)]
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    create_kpi_cards(df_filtered)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_charts(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_team_performance(df_filtered), use_container_width=True)
    
    # Regional analysis
    st.plotly_chart(create_regional_analysis(df_filtered), use_container_width=True)
    
    # Data table
    with st.expander("📋 Raw Data"):
        st.dataframe(df_filtered.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 ABDULLAH FOUAD COMPANY - Advanced Analytics Dashboard</p>
        <p>Powered by Streamlit & Plotly | Real-time Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()