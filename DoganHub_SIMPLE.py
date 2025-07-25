#!/usr/bin/env python3
"""
🚀 DOGANHUB - ONE SIMPLE SYSTEM
===============================
Fixed structure - no more new folders created automatically
"""

import os
import sys
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

class DoganHubSimple:
    """One simple system - fixed structure"""

    def __init__(self):
        # FIXED PATHS - NO MORE NEW FOLDERS
        self.root_dir = Path("d:/DoganLab")
        self.data_dir = self.root_dir / "data"
        self.output_dir = self.root_dir / "outputs"

        # Use existing data files
        self.opportunity_file = self.data_dir / "Opportunity Hub.csv"

        print("🚀 DoganHub Simple System Started")
        print(f"📁 Data: {self.data_dir}")
        print(f"📁 Output: {self.output_dir}")
        print("=" * 50)

    def load_data(self):
        """Load data from existing files only"""
        try:
            if self.opportunity_file.exists():
                self.df = pd.read_csv(self.opportunity_file)
                print(f"✅ Loaded {len(self.df)} opportunities")
                return True
            else:
                print("❌ No data file found")
                return False
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False

    def create_dashboard(self):
        """Create simple dashboard"""
        if not hasattr(self, 'df'):
            if not self.load_data():
                return

        st.set_page_config(
            page_title="DoganHub Dashboard",
            page_icon="🚀",
            layout="wide"
        )

        st.title("🚀 DoganHub Dashboard")
        st.markdown("---")

        # Basic metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Opportunities", len(self.df))

        with col2:
            if 'Amount' in self.df.columns:
                total_value = self.df['Amount'].sum()
                st.metric("Total Value", f"${total_value:,.0f}")

        with col3:
            if 'Stage' in self.df.columns:
                won_count = len(self.df[self.df['Stage'].str.contains('Won', na=False)])
                st.metric("Won Deals", won_count)

        with col4:
            if 'Owner' in self.df.columns:
                unique_owners = self.df['Owner'].nunique()
                st.metric("Sales People", unique_owners)

        # Simple charts
        if 'Stage' in self.df.columns:
            st.subheader("📊 Pipeline by Stage")
            stage_counts = self.df['Stage'].value_counts()
            fig = px.bar(x=stage_counts.index, y=stage_counts.values)
            st.plotly_chart(fig, use_container_width=True)

        if 'Owner' in self.df.columns and 'Amount' in self.df.columns:
            st.subheader("💰 Revenue by Owner")
            owner_revenue = self.df.groupby('Owner')['Amount'].sum().sort_values(ascending=False)
            fig = px.bar(x=owner_revenue.index, y=owner_revenue.values)
            st.plotly_chart(fig, use_container_width=True)

    def run_analysis(self):
        """Run simple analysis without creating new folders"""
        if not self.load_data():
            return

        print("\n📊 ANALYSIS RESULTS")
        print("=" * 30)

        # Basic stats
        print(f"Total Opportunities: {len(self.df)}")

        if 'Amount' in self.df.columns:
            total_value = self.df['Amount'].sum()
            print(f"Total Pipeline Value: ${total_value:,.0f}")

        if 'Stage' in self.df.columns:
            print("\nPipeline by Stage:")
            stage_counts = self.df['Stage'].value_counts()
            for stage, count in stage_counts.items():
                print(f"  {stage}: {count}")

        if 'Owner' in self.df.columns:
            print(f"\nSales People: {self.df['Owner'].nunique()}")

        print("\n✅ Analysis Complete - No new folders created!")

def main():
    """Main function"""
    system = DoganHubSimple()

    # Check if running in Streamlit
    if len(sys.argv) > 1 and sys.argv[1] == "dashboard":
        system.create_dashboard()
    else:
        system.run_analysis()

if __name__ == "__main__":
    main()
