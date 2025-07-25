import streamlit as st
import pandas as pd

def data_connector():
    st.title("🔌 Connect to Data Source")
    source = st.selectbox("Choose source", ["CSV", "Excel", "Google Sheets", "Snowflake", "BigQuery", "REST API"])
    if source == "CSV":
        file = st.file_uploader("Upload CSV")
        if file:
            df = pd.read_csv(file)
            st.session_state["df"] = df
            st.dataframe(df.head())
    elif source == "Google Sheets":
        url = st.text_input("Google Sheet URL")
        if url and st.button("Load"):
            sheet_id = url.split('/')[5]
            sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
            df = pd.read_csv(sheet_url)
            st.session_state["df"] = df
            st.dataframe(df.head())
    # Add more connectors as you wish!