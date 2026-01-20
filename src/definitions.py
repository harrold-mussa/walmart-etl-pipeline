import pandas as pd
import os

def extract(store_data, extra_data):
  extra_df = pd.read_parquet(extra_data)
  merged_df = store_data.merge(extra_df, on="index")
  return merged_df

merged_df = extract(grocery_sales, "extra_data.parquet")

def transform(raw_data):
  raw_data.fillna(
    {
      'CPI': raw_data['CPI'].mean(),
      'Weekly_Sales': raw_data['Weekly_Sales'].mean(),
      'Unemployment': raw_data['Unemployment'].mean()
    }, inplace=True
  )

  raw_data['Date'] = pd.to_datetime(raw_data['Date'] = '%Y-%m-%d'
  raw_data['Month'] = raw_data['Date'].dt.month
  raw_data = raw_data.loc[raw_data['Weekly_Sales'] > 10000, :]
  raw_data = raw_data.drop(['index', 'Temperature', 'Fuel_Price', 'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'Type', 'Size', 'Date'], axis=1)
  return raw_data

clean_data = transform(merged_df)
  
