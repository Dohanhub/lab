"""
🎨 DoganHub/AFCO Corporate Branding System
======================================

Complete branding and theming system for DoganHub MSI applications
with corporate colors, logos, and visual identity guidelines.
"""

import streamlit as st
import base64
from pathlib import Path

# AFCO/DoganHub Corporate Color Palette
DoganHub_COLORS = {
    'primary': '#002D72',      # Navy Blue
    'accent': '#C8A951',       # Gold
    'secondary': '#4A4A4A',    # Slate/Graphite Gray
    'background': '#F5F6FA',   # Light Gray/White
    'error': '#C0392B',        # Dark Red
    'success': '#2ECC71',      # DoganHub Green
    'warning': '#F39C12',      # Orange
    'info': '#3498DB',         # Blue
    'white': '#FFFFFF',
    'black': '#000000'
}

def apply_doganhub_branding():
    """تطبيق العلامة التجارية DoganHub"""

    # Prevent flickering by checking if already applied
    if 'doganhub_branding_applied' not in st.session_state:
        st.session_state.doganhub_branding_applied = True

        st.markdown(f"""
        <style>
        /* DoganHub Corporate Theme - Stable Version */
        .stApp {{
            background-color: {DoganHub_COLORS['background']} !important;
        }}

    /* Header Styling */
    .doganhub-header {{
        background: linear-gradient(135deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['secondary']} 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 45, 114, 0.3);
    }}

    .doganhub-header h1 {{
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
    }}

    .doganhub-header p {{
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
        color: white;
    }}

    /* Primary Buttons */
    .stButton > button {{
        background: linear-gradient(135deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['accent']} 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 45, 114, 0.2);
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 45, 114, 0.3);
    }}

    /* Metrics Cards */
    .metric-card {{
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border-left: 4px solid {DoganHub_COLORS['primary']};
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }}

    /* Feature Cards */
    .doganhub-feature-card {{
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }}

    .doganhub-feature-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['accent']} 100%);
    }}

    .doganhub-feature-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }}

    /* Sidebar Styling */
    .css-1d391kg {{
        background: linear-gradient(180deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['secondary']} 100%);
    }}

    /* Fix Sidebar Visibility */
    .css-1lcbmhc {{
        background-color: {DoganHub_COLORS['primary']} !important;
        color: white !important;
    }}

    .css-17eq0hr {{
        background-color: {DoganHub_COLORS['primary']} !important;
        color: white !important;
    }}

    /* Sidebar Text Color Fix */
    .css-1d391kg .css-10trblm {{
        color: white !important;
    }}

    .css-1d391kg .css-1cpxqw2 {{
        color: white !important;
    }}

    /* Option Menu Styling */
    .nav-link-selected {{
        background-color: {DoganHub_COLORS['accent']} !important;
        color: white !important;
    }}

    .nav-link {{
        color: white !important;
        background-color: transparent !important;
    }}

    .nav-link:hover {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }}

    /* Navigation Menu */
    .nav-link {{
        color: white !important;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin: 0.25rem 0;
        transition: all 0.3s ease;
    }}

    .nav-link:hover {{
        background: rgba(255, 255, 255, 0.1);
        transform: translateX(5px);
    }}

    .nav-link.active {{
        background: {DoganHub_COLORS['accent']};
        color: white !important;
    }}

    /* Success/Error Messages */
    .stSuccess {{
        background-color: {DoganHub_COLORS['success']};
        color: white;
        border-radius: 10px;
    }}

    .stError {{
        background-color: {DoganHub_COLORS['error']};
        color: white;
        border-radius: 10px;
    }}

    .stWarning {{
        background-color: {DoganHub_COLORS['warning']};
        color: white;
        border-radius: 10px;
    }}

    .stInfo {{
        background-color: {DoganHub_COLORS['info']};
        color: white;
        border-radius: 10px;
    }}

    /* Tables */
    .dataframe {{
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }}

    .dataframe th {{
        background: {DoganHub_COLORS['primary']} !important;
        color: white !important;
        font-weight: 600;
    }}

    /* Charts */
    .js-plotly-plot {{
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}

    .stTabs [data-baseweb="tab"] {{
        background: {DoganHub_COLORS['primary']};
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }}

    .stTabs [aria-selected="true"] {{
        background: {DoganHub_COLORS['accent']} !important;
        color: white !important;
    }}

    /* Expanders */
    .streamlit-expanderHeader {{
        background: {DoganHub_COLORS['primary']};
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }}

    /* Progress Bars */
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['accent']} 100%);
    }}

    /* Selectbox */
    .stSelectbox > div > div {{
        background: white;
        border: 2px solid {DoganHub_COLORS['primary']};
        border-radius: 8px;
    }}

    /* Text Input */
    .stTextInput > div > div > input {{
        border: 2px solid {DoganHub_COLORS['primary']};
        border-radius: 8px;
    }}

    /* File Uploader */
    .stFileUploader > div > div {{
        border: 2px dashed {DoganHub_COLORS['primary']};
        border-radius: 10px;
        background: rgba(0, 45, 114, 0.05);
    }}

    /* Hide Streamlit Branding */
    #MainMenu {{visibility: hidden !important;}}
    footer {{visibility: hidden !important;}}
    header {{visibility: hidden !important;}}

    /* Prevent Theme Flickering */
    .stApp > div {{
        transition: none !important;
    }}

    .css-1d391kg {{
        transition: none !important;
    }}

    /* Custom DoganHub Logo Area */
    .doganhub-logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }}

    /* Status Indicators */
    .status-indicator {{
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }}

    .status-online {{
        background: {DoganHub_COLORS['success']};
        box-shadow: 0 0 10px {DoganHub_COLORS['success']};
    }}

    .status-warning {{
        background: {DoganHub_COLORS['warning']};
        box-shadow: 0 0 10px {DoganHub_COLORS['warning']};
    }}

    .status-error {{
        background: {DoganHub_COLORS['error']};
        box-shadow: 0 0 10px {DoganHub_COLORS['error']};
    }}

    /* Responsive Design */
    @media (max-width: 768px) {{
        .doganhub-header h1 {{
            font-size: 2rem;
        }}

        .doganhub-feature-card {{
            padding: 1rem;
        }}

        .metric-card {{
            padding: 1rem;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

def show_doganhub_header(title, subtitle=None, icon="🎯"):
    """عرض رأس DoganHub المخصص"""

    subtitle_html = f"<p>{subtitle}</p>" if subtitle else ""

    st.markdown(f"""
    <div class="doganhub-header">
        <h1>{icon} {title}</h1>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)

def show_doganhub_logo():
    """عرض شعار DoganHub"""

    # Try to load logo, fallback to text if not found
    logo_path = Path("assets/doganhub_logo.png")

    if logo_path.exists():
        st.image(str(logo_path), width=150)
    else:
        # Fallback to styled text logo
        st.markdown("""
        <div class="doganhub-logo-container">
            <div style="text-align: center;">
                <h2 style="margin: 0; color: #002D72; font-weight: 700;">DoganHub</h2>
                <p style="margin: 0; color: #C8A951; font-size: 0.9rem; font-weight: 600;">MSI</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_metric_card(title, value, delta=None, icon="📊", color="primary"):
    """إنشاء بطاقة مقياس DoganHub"""

    color_value = DoganHub_COLORS.get(color, DoganHub_COLORS['primary'])
    delta_html = f"<p style='color: {color_value}; margin: 0.5rem 0 0 0; font-weight: 600;'>{delta}</p>" if delta else ""

    return f"""
    <div class="metric-card">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <h3 style="margin: 0; color: {color_value}; font-size: 1.1rem;">{title}</h3>
                <h2 style="margin: 0.5rem 0; color: #333; font-size: 2rem; font-weight: 700;">{value}</h2>
                {delta_html}
            </div>
            <div style="font-size: 2.5rem; opacity: 0.7;">{icon}</div>
        </div>
    </div>
    """

def create_feature_card(title, description, icon="🎯", button_text=None, button_key=None):
    """إنشاء بطاقة ميزة DoganHub"""

    button_html = ""
    if button_text and button_key:
        button_html = f"""
        <div style="margin-top: 1.5rem;">
            <button onclick="document.getElementById('{button_key}').click()"
                    style="background: linear-gradient(135deg, {DoganHub_COLORS['primary']} 0%, {DoganHub_COLORS['accent']} 100%);
                           color: white; border: none; border-radius: 8px; padding: 0.75rem 1.5rem;
                           font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                {button_text}
            </button>
        </div>
        """

    return f"""
    <div class="doganhub-feature-card">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <h3 style="margin: 0; color: {DoganHub_COLORS['primary']}; font-size: 1.4rem; font-weight: 700;">{title}</h3>
        </div>
        <div style="color: #666; line-height: 1.6; text-align: center;">
            {description}
        </div>
        {button_html}
    </div>
    """

def show_status_indicator(status, text):
    """عرض مؤشر الحالة"""

    status_classes = {
        'online': 'status-online',
        'warning': 'status-warning',
        'error': 'status-error'
    }

    status_class = status_classes.get(status, 'status-online')

    return f"""
    <div style="display: flex; align-items: center; margin: 0.5rem 0;">
        <span class="status-indicator {status_class}"></span>
        <span style="color: #333; font-weight: 500;">{text}</span>
    </div>
    """

def apply_rtl_support():
    """دعم الكتابة من اليمين لليسار"""

    st.markdown("""
    <style>
    /* RTL Support for Arabic */
    .rtl {
        direction: rtl;
        text-align: right;
    }

    .rtl .stSelectbox > div > div {
        text-align: right;
    }

    .rtl .stTextInput > div > div > input {
        text-align: right;
    }

    .rtl .stTextArea > div > div > textarea {
        text-align: right;
    }

    /* Arabic Font Support */
    .arabic-text {
        font-family: 'Segoe UI', 'Tahoma', 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

def get_doganhub_color_palette():
    """الحصول على لوحة ألوان DoganHub"""
    return DoganHub_COLORS

def create_doganhub_chart_theme():
    """إنشاء موضوع الرسوم البيانية DoganHub"""

    return {
        'layout': {
            'colorway': [
                DoganHub_COLORS['primary'],
                DoganHub_COLORS['accent'],
                DoganHub_COLORS['success'],
                DoganHub_COLORS['info'],
                DoganHub_COLORS['warning'],
                DoganHub_COLORS['secondary']
            ],
            'paper_bgcolor': DoganHub_COLORS['white'],
            'plot_bgcolor': DoganHub_COLORS['background'],
            'font': {
                'family': 'Segoe UI, Tahoma, Arial, sans-serif',
                'size': 12,
                'color': DoganHub_COLORS['black']
            },
            'title': {
                'font': {
                    'size': 18,
                    'color': DoganHub_COLORS['primary']
                }
            }
        }
    }

# Export functions for easy import
__all__ = [
    'apply_doganhub_branding',
    'show_doganhub_header',
    'show_doganhub_logo',
    'create_metric_card',
    'create_feature_card',
    'show_status_indicator',
    'apply_rtl_support',
    'get_doganhub_color_palette',
    'create_doganhub_chart_theme',
    'DoganHub_COLORS'
]
