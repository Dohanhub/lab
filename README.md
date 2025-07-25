# Advanced Data Analytics & ML Dashboard

A powerful, interactive Streamlit dashboard for exploring, visualizing, and modeling your data.  
Supports advanced features like anomaly detection, clustering, forecasting (Prophet), classification, regression, explainability (SHAP), model export, and prediction export.  
Works with CSV and Excel files. Optional Snowflake integration.

---

## Features

- **Data Exploration:** Preview, stats, missing values, KPIs.
- **Visualizations:** Histograms, boxplots, pairplots, heatmaps, time series, categorical breakdowns.
- **Anomaly Detection:** Isolation Forest outlier detection.
- **Clustering:** KMeans clustering and plotting.
- **Forecasting:** Prophet-based time series forecasting.
- **ML Modeling:** Classification (Random Forest, XGBoost, LightGBM, Logistic Regression, SVM), Regression (Random Forest, XGBoost, LightGBM, Linear Regression, SVR).
- **Explainability:** SHAP summary plots for feature importance.
- **Model Export:** Download trained models (`.pkl`).
- **Prediction Export:** Download predictions (`.csv`).
- **Snowflake Integration:** Optional module to fetch data from Snowflake.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

### 2. Prepare Data

- Place your `.csv` or `.xlsx` files in a folder (e.g., `data/`).

---

### 3. Environment Setup

#### **A. Using Conda**

Recommended for most users.

```bash
conda env create -f environment.yml
conda activate ml-dashboard
```

#### **B. Using pip**

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

```bash
streamlit run app.py
```

- Enter your data folder path in the sidebar.
- Select a file and explore the dashboard tabs.

---

### 5. Optional: Snowflake Integration

- Install Snowflake connector if needed:
  ```bash
  pip install snowflake-connector-python
  ```
- Use `snowflake_loader.py` to load data from Snowflake.  
  Edit the credentials and query as needed.

---

### 6. Model Export/Prediction Export

- After training a model (ML & Explainability tab), use the download buttons to export the trained model (`.pkl`) and predictions (`.csv`).
- These can be loaded elsewhere using `joblib` or in your favorite notebook.

---

## Requirements

- Python 3.10+
- See `environment.yml` (for Conda) or `requirements.txt` (for pip).

**Main packages:**
- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- lightgbm
- openpyxl
- prophet
- shap
- joblib
- (optional) snowflake-connector-python

---

## Extending the Dashboard

- To add new ML algorithms:  
  Edit or extend the ML/modeling section in `app.py` or `ml_advanced.py`.
- For more explainability:  
  Integrate with SHAP, LIME, or your favorite library.
- For other data sources:  
  Add loader utilities as in `snowflake_loader.py`.

---

## Project Files Overview

| File                  | Purpose                                              |
|-----------------------|------------------------------------------------------|
| `app.py`              | Main Streamlit dashboard                             |
| `ml_advanced.py`      | (Optional) Modular advanced ML and exports           |
| `snowflake_loader.py` | (Optional) Snowflake data loader utility             |
| `environment.yml`     | Conda environment specification                      |
| `requirements.txt`    | pip requirements list                                |
| `README.md`           | This documentation                                   |

---

## Moving Forward

- Add new data by placing files in your data folder.
- Add new ML features by extending the appropriate tab in `app.py`.
- For cloud deployment, see [Streamlit sharing](https://streamlit.io/cloud) or Dockerize your app.
- For enterprise data, use `snowflake_loader.py` to connect to Snowflake.

---

## Need help?

- [Streamlit documentation](https://docs.streamlit.io/)
- [scikit-learn documentation](https://scikit-learn.org/)
- [XGBoost documentation](https://xgboost.readthedocs.io/)
- [LightGBM documentation](https://lightgbm.readthedocs.io/)