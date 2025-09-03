import pandas as pd
import requests

# ===========================================
# Data Integration & ETL Pipeline Project
# Author: Syamala Makireddi
# ===========================================

# Step 1: Extract
# Here we simulate data extraction from a CSV file.
# (In a real project, this could be from REST APIs, AWS S3, or databases.)
df = pd.read_csv("sample_data.csv")
print("Extracted Data:")
print(df.head())

# Step 2: Transform
# Clean the data: drop missing values, normalize column names, apply transformations
df.columns = [col.lower() for col in df.columns]
df = df.dropna()  # remove rows with missing values

# Example transformation: convert all customer names to uppercase
df["name"] = df["name"].str.upper()

# Example transformation: calculate loyalty points (10% of purchase amount)
df["loyalty_points"] = df["purchaseamount"] * 0.10

print("\nTransformed Data:")
print(df.head())

# Step 3: Load
# Save the cleaned and transformed data into a new file (could be a DB in real project)
df.to_csv("clean_data.csv", index=False)
print("\nData successfully saved to clean_data.csv")
