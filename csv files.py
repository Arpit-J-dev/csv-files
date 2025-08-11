# Task 5: Data Analysis on CSV Files
# Objective: Analyze sales data using Pandas

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
# Replace 'sales_data.csv' with your actual CSV file name
df = pd.read_csv('sales_data.csv')

# 2. Data Exploration
print("First 5 rows of data:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 3. Data Analysis (Example: Group sales by Product)
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
print("\nTotal Sales by Product:")
print(sales_by_product)

# 4. Visualization: Sales by Product (Bar Chart)
plt.figure(figsize=(8, 5))
plt.bar(sales_by_product['Product'], sales_by_product['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Visualization: Sales Trend over Time (if Date column exists)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    sales_over_time = df.groupby('Date')['Sales'].sum().reset_index()
    
    plt.figure(figsize=(10, 5))
    plt.plot(sales_over_time['Date'], sales_over_time['Sales'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.title('Sales Trend Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
