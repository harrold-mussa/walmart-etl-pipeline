import pandas as pd
import os

def avg_weekly_sales_per_month(clean_data):
    holidays_sales = clean_data[["Month", "Weekly_Sales"]]
    holidays_sales = (holidays_sales.groupby("Month").agg(Avg_Sales = ("Weekly_Sales", "mean")).reset_index().round(2))
    return holidays_sales

agg_data = avg_weekly_sales_per_month(clean_data)

def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    full_data.to_csv(full_data_file_path, index = False)
    agg_data.to_csv(agg_data_file_path, index = False)

load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")

def validation(file_path):
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"There is no file at the path {file_path}")

validation("clean_data.csv")
validation("agg_data.csv")