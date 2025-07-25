"""
Agent Instruction:

This script analyzes sales performance by processing invoice files across years.
- It maps coded employee numbers to names
- Aggregates actual sales
- Joins them with targets
- Calculates variance and achievement %
"""
import pandas as pd
import glob
import os

# 1. Read all invoice files
invoice_files = glob.glob(os.path.join("Invoices 2025", "*.xlsx"))
all_invoices = []
for file in invoice_files:
    df = pd.read_excel(file)
    all_invoices.append(df)

# 2. Concatenate all data
invoices = pd.concat(all_invoices, ignore_index=True)

# 3. Map Employee Number to Employee Name
# Please update the path to Employees.xlsx as needed
employees_path = "Employees.xlsx"
if not os.path.exists(employees_path):
    raise FileNotFoundError("Employees.xlsx not found. Please add the employee mapping file to the workspace.")

employees = pd.read_excel(employees_path)
invoices = invoices.merge(employees, on="Employee Number", how="left")

# 4. Add Month and Year columns (bonus)
invoices["Date"] = pd.to_datetime(invoices["Date"])
invoices["Month"] = invoices["Date"].dt.month
invoices["Year"] = invoices["Date"].dt.year

# 5. Group by Employee Name and sum Invoice Value
actuals = invoices.groupby(["Employee Name", "Employee Number"], as_index=False)["Invoice Value"].sum()
actuals = actuals.rename(columns={"Invoice Value": "Actual"})

# 6. Read Target.xlsx and match by Employee Name
targets = pd.read_excel(os.path.join("2025 Targetet KPIS", "Target.xlsx"))
report = targets.merge(actuals, on="Employee Name", how="left")

# 7. Fill missing Actuals with 0, get Employee Number from actuals if missing
report["Actual"] = report["Actual"].fillna(0)
if "Employee Number_y" in report.columns:
    report["Employee Number"] = report["Employee Number_y"].combine_first(report["Employee Number_x"])
    report = report.drop(columns=["Employee Number_x", "Employee Number_y"])

# 8. Calculate Variance and Achievement %
report["Variance"] = report["Actual"] - report["Target"]
report["Achievement %"] = (report["Actual"] / report["Target"]) * 100

# 9. Export to Excel
report.to_excel("Summary_Report.xlsx", index=False)

print("Summary_Report.xlsx generated successfully.")
