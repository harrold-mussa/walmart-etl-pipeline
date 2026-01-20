import pandas as pd
import os

def extract(store_data, extra_data):
  extra_df = pd.read_parquet(extra_data)
  merged_df = store_data.merge(extra_df, on="index")
  return merged_df

merged_df = extract(grocery_sales, "extra_data.parquet")
  
