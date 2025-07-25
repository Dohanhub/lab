# 🚀 Advanced KPI Dashboard

A comprehensive Streamlit-based dashboard for tracking Sales, Presales, Finance, and Sales Operations KPIs with manual data update capabilities.

## 📊 Features

### Dashboard Sections
1. **Sales Performance**
   - Monthly Revenue Trend
   - Deals Closed vs Target Achievement
   - Average Deal Size Analysis
   - Sales Cycle & Conversion Rate Tracking

2. **Presales Performance**
   - Lead Generation Funnel
   - Pipeline Value Trend
   - Lead Qualification Rate
   - Demo Conversion & Proposal Win Rates

3. **Financial Performance**
   - Margin Analysis (Gross & Operating)
   - Monthly Cash Flow
   - Accounts Receivable & Collection Period
   - Budget Variance Tracking

4. **Sales Operations**
   - Forecast Accuracy vs Quota Attainment
   - Sales Productivity Index
   - Activity Metrics & Territory Performance
   - Customer Churn Rate

5. **Data Input & Updates**
   - Manual data entry for all departments
   - Real-time dashboard updates
   - Data persistence in JSON format

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

#### Option 1: Using Batch File (Windows)
```bash
# Double-click run_dashboard.bat
# Or run from command prompt:
run_dashboard.bat
```

#### Option 2: Using PowerShell (Windows)
```powershell
# Run from PowerShell:
.\run_dashboard.ps1
```

#### Option 3: Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run advanced_kpi_dashboard.py
```

## 📈 Using the Dashboard

### Navigation
- Use the sidebar to navigate between different dashboard views
- Select "Overview" for a combined view of key metrics
- Choose specific departments for detailed analysis
- Use "Data Input" to manually update KPI data

### Data Updates
1. Navigate to "Data Input" section
2. Select the department you want to update
3. Enter new KPI values in the form
4. Click "Update [Department] Data" button
5. Dashboard will refresh automatically with new data

### Key Metrics Tracked

#### Sales KPIs
- Monthly Revenue ($)
- Deals Closed (count)
- Average Deal Size ($)
- Conversion Rate (%)
- Sales Cycle (days)
- Target Achievement (%)

#### Presales KPIs
- Leads Generated (count)
- Qualified Leads (count)
- Lead Qualification Rate (%)
- Demo Conversion Rate (%)
- Proposal Win Rate (%)
- Pipeline Value ($)

#### Finance KPIs
- Gross Margin (%)
- Operating Margin (%)
- Cash Flow ($)
- Accounts Receivable ($)
- Collection Period (days)
- Budget Variance (%)

#### Sales Operations KPIs
- Forecast Accuracy (%)
- Quota Attainment (%)
- Activity Metrics (count)
- Territory Performance (%)
- Sales Productivity (index)
- Churn Rate (%)

## 💾 Data Storage

- Data is stored in `kpi_data.json` file
- Automatic backup on each update
- Sample data is provided for initial setup
- Data persists between dashboard sessions

## 🎨 Dashboard Features

### Visual Elements
- Interactive Plotly charts
- Real-time metric cards
- Color-coded performance indicators
- Responsive design for different screen sizes

### Chart Types
- Line charts for trend analysis
- Bar charts for comparative data
- Area charts for cumulative metrics
- Funnel charts for conversion analysis
- Dual-axis charts for correlation analysis

## 🔧 Customization

### Adding New KPIs
1. Edit the `create_default_data()` method in `advanced_kpi_dashboard.py`
2. Add new KPI fields to the appropriate department section
3. Update the corresponding dashboard rendering method
4. Add input fields in the data input section

### Styling Modifications
- Modify the CSS in the `st.markdown()` section at the top of the file
- Adjust colors, fonts, and layout as needed
- Plotly chart styling can be customized in each chart creation function

## 📱 Access

Once running, the dashboard will be available at:
- Local URL: `http://localhost:8501`
- Network URL: `http://[your-ip]:8501`

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   streamlit run advanced_kpi_dashboard.py --server.port 8502
   ```

2. **Missing Dependencies**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Data File Issues**
   - Delete `kpi_data.json` to reset to default data
   - Check file permissions in the project directory

### Performance Tips
- Keep data history reasonable (6-12 months for optimal performance)
- Use the data input section to add data incrementally
- Refresh browser if charts don't update properly

## 📊 Sample Data

The dashboard comes with 6 months of sample data across all departments. This data demonstrates:
- Realistic KPI trends
- Seasonal variations
- Performance improvements over time
- Correlation between different metrics

## 🔄 Updates & Maintenance

### Regular Maintenance
- Backup `kpi_data.json` regularly
- Monitor dashboard performance with large datasets
- Update dependencies periodically

### Future Enhancements
- Database integration (SQL Server, PostgreSQL)
- Automated data imports from CRM/ERP systems
- Email reporting capabilities
- Advanced analytics and forecasting
- User authentication and role-based access

## 📞 Support

For issues or feature requests:
1. Check the troubleshooting section
2. Review the code comments for customization guidance
3. Test with sample data to isolate issues

---

**Dashboard Version:** 1.0  
**Last Updated:** December 2024  
**Compatible with:** Streamlit 1.28+, Python 3.7+# 🚀 Advanced KPI Dashboard

A comprehensive Streamlit-based dashboard for tracking Sales, Presales, Finance, and Sales Operations KPIs with manual data update capabilities.

## 📊 Features

### Dashboard Sections
1. **Sales Performance**
   - Monthly Revenue Trend
   - Deals Closed vs Target Achievement
   - Average Deal Size Analysis
   - Sales Cycle & Conversion Rate Tracking

2. **Presales Performance**
   - Lead Generation Funnel
   - Pipeline Value Trend
   - Lead Qualification Rate
   - Demo Conversion & Proposal Win Rates

3. **Financial Performance**
   - Margin Analysis (Gross & Operating)
   - Monthly Cash Flow
   - Accounts Receivable & Collection Period
   - Budget Variance Tracking

4. **Sales Operations**
   - Forecast Accuracy vs Quota Attainment
   - Sales Productivity Index
   - Activity Metrics & Territory Performance
   - Customer Churn Rate

5. **Data Input & Updates**
   - Manual data entry for all departments
   - Real-time dashboard updates
   - Data persistence in JSON format

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

#### Option 1: Using Batch File (Windows)
```bash
# Double-click run_dashboard.bat
# Or run from command prompt:
run_dashboard.bat
```

#### Option 2: Using PowerShell (Windows)
```powershell
# Run from PowerShell:
.\run_dashboard.ps1
```

#### Option 3: Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run advanced_kpi_dashboard.py
```

## 📈 Using the Dashboard

### Navigation
- Use the sidebar to navigate between different dashboard views
- Select "Overview" for a combined view of key metrics
- Choose specific departments for detailed analysis
- Use "Data Input" to manually update KPI data

### Data Updates
1. Navigate to "Data Input" section
2. Select the department you want to update
3. Enter new KPI values in the form
4. Click "Update [Department] Data" button
5. Dashboard will refresh automatically with new data

### Key Metrics Tracked

#### Sales KPIs
- Monthly Revenue ($)
- Deals Closed (count)
- Average Deal Size ($)
- Conversion Rate (%)
- Sales Cycle (days)
- Target Achievement (%)

#### Presales KPIs
- Leads Generated (count)
- Qualified Leads (count)
- Lead Qualification Rate (%)
- Demo Conversion Rate (%)
- Proposal Win Rate (%)
- Pipeline Value ($)

#### Finance KPIs
- Gross Margin (%)
- Operating Margin (%)
- Cash Flow ($)
- Accounts Receivable ($)
- Collection Period (days)
- Budget Variance (%)

#### Sales Operations KPIs
- Forecast Accuracy (%)
- Quota Attainment (%)
- Activity Metrics (count)
- Territory Performance (%)
- Sales Productivity (index)
- Churn Rate (%)

## 💾 Data Storage

- Data is stored in `kpi_data.json` file
- Automatic backup on each update
- Sample data is provided for initial setup
- Data persists between dashboard sessions

## 🎨 Dashboard Features

### Visual Elements
- Interactive Plotly charts
- Real-time metric cards
- Color-coded performance indicators
- Responsive design for different screen sizes

### Chart Types
- Line charts for trend analysis
- Bar charts for comparative data
- Area charts for cumulative metrics
- Funnel charts for conversion analysis
- Dual-axis charts for correlation analysis

## 🔧 Customization

### Adding New KPIs
1. Edit the `create_default_data()` method in `advanced_kpi_dashboard.py`
2. Add new KPI fields to the appropriate department section
3. Update the corresponding dashboard rendering method
4. Add input fields in the data input section

### Styling Modifications
- Modify the CSS in the `st.markdown()` section at the top of the file
- Adjust colors, fonts, and layout as needed
- Plotly chart styling can be customized in each chart creation function

## 📱 Access

Once running, the dashboard will be available at:
- Local URL: `http://localhost:8501`
- Network URL: `http://[your-ip]:8501`

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   streamlit run advanced_kpi_dashboard.py --server.port 8502
   ```

2. **Missing Dependencies**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Data File Issues**
   - Delete `kpi_data.json` to reset to default data
   - Check file permissions in the project directory

### Performance Tips
- Keep data history reasonable (6-12 months for optimal performance)
- Use the data input section to add data incrementally
- Refresh browser if charts don't update properly

## 📊 Sample Data

The dashboard comes with 6 months of sample data across all departments. This data demonstrates:
- Realistic KPI trends
- Seasonal variations
- Performance improvements over time
- Correlation between different metrics

## 🔄 Updates & Maintenance

### Regular Maintenance
- Backup `kpi_data.json` regularly
- Monitor dashboard performance with large datasets
- Update dependencies periodically

### Future Enhancements
- Database integration (SQL Server, PostgreSQL)
- Automated data imports from CRM/ERP systems
- Email reporting capabilities
- Advanced analytics and forecasting
- User authentication and role-based access

## 📞 Support

For issues or feature requests:
1. Check the troubleshooting section
2. Review the code comments for customization guidance
3. Test with sample data to isolate issues

---

**Dashboard Version:** 1.0  
**Last Updated:** December 2024  
**Compatible with:** Streamlit 1.28+, Python 3.7+