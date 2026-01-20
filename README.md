# Project Background 

## Overview

I have built a data pipeline using custom functions to extract, transform, aggregate, and load e-commerce data. The SQL query for grocery_sales and the extract() function have been added in a separate folder. 

## Goal

The project implements a function named `transform()` with one argument, taking `merged_df` as input, filling missing numerical values, adding a column "Month", keeping the rows where the weekly sales are over $10,000 and drops the unnecessary columns. Ultimately, it returns a DataFrame and be stored as the `clean_data` variable.

Afterwards, there is the function `avg_weekly_sales_per_month` with one argument, taking `clean_data` as input. This function will calculate the average monthly sales. To implement this function, I selected the "Month" and "Weekly_Sales" columns as they are the only ones needed for this analysis, then I created a chain operation with `groupby()`, `agg()`, `reset_index()`, and `round()` functions, then grouped by the "Month" column and calculated the average monthly sales, then called `reset_index()` to start a new index order and finally rounded the results to two decimal places.

The function called `load()` is then created that takes the cleaned and aggregated DataFrames, and their paths, and saves them as `clean_data.csv` and `agg_data.csv` respectively, without an index.

Lastly, I defined a `validation()` function that checks whether the two csv files from the `load()` exist in the current working directory.


