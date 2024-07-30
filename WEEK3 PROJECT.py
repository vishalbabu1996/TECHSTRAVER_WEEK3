# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from collections import Counter

# Load the dataset
url = 'https://drive.google.com/file/d/135oJXw-npofrkmHAnCJDbF9ZHdI5eGNe/view?usp=sharing'
data = pd.read_csv(url)

# Display the first few rows of the dataset
print("Data Loaded:")
print(data.head())

# Clean and Preprocess Data
# Handle missing values
print("\nHandling missing values...")
data = data.dropna()

# Remove duplicate entries
print("Removing duplicates...")
data = data.drop_duplicates()

# Convert Date column to Datetime type
print("Converting Date column to Datetime...")
data['Date'] = pd.to_datetime(data['Date'])

# Extract month and year from the Date
data['month'] = data['Date'].dt.month
data['year'] = data['Date'].dt.year

# Display the upDated dataframe
print("\nUpDated DataFrame:")
print(data.head())

# Conduct Exploratory Data Analysis (EDA)
# Descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Visualizations
# Sales per month
monthly_sales = data.groupby('month').sum()['sales']
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# City with the Most Product Sales
city_sales = data.groupby('ship-city').sum()['sales']
plt.figure(figsize=(10, 6))
city_sales.plot(kind='bar')
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.show()

# Optimal Advertisement Timing
data['hour'] = data['Date'].dt.hour
hourly_sales = data.groupby('hour').sum()['sales']
plt.figure(figsize=(10, 6))
hourly_sales.plot(kind='bar')
plt.title('Hourly Sales')
plt.xlabel('Hour')
plt.ylabel('Sales')
plt.show()

# Products Sold Together
order_product = data.groupby('order_id')['product'].apply(list)
product_combinations = Counter()
for products in order_product:
    product_combinations.upDate(Counter(combinations(products, 2)))
most_common_combinations = product_combinations.most_common(5)
print("\nMost commonly sold together products:")
print(most_common_combinations)

# Top-Selling Product
top_product = data.groupby('product').sum()['sales'].idxmax()
top_product_sales = data.groupby('product').sum()['sales'].max()
print(f"\nThe top-selling product is {top_product} with total sales of {top_product_sales}.")

# Least Selling Product by Category and Brand
least_selling_product = data.groupby(['category', 'brand']).sum()['sales'].idxmin()
least_selling_product_sales = data.groupby(['category', 'brand']).sum()['sales'].min()
print(f"The least selling product by category and brand is {least_selling_product} with total sales of {least_selling_product_sales}.")

# Ratings Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['rating'], bins=20, kde=True)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Best Rated Brands
best_rated_brands = data.groupby('brand').mean()['rating'].sort_values(ascending=False).head(5)
print("\nBest rated brands:")
print(best_rated_brands)

# Draw Conclusions and Insights
# Best Month for Sales
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()
print(f"\nThe best month for sales is {best_month} with total sales of {best_month_sales}.")

# City with the Most Product Sales
best_city = city_sales.idxmax()
best_city_sales = city_sales.max()
print(f"The city with the most product sales is {best_city} with total sales of {best_city_sales}.")

# Optimal Advertisement Timing
peak_hour = hourly_sales.idxmax()
peak_hour_sales = hourly_sales.max()
print(f"The peak hour for sales is {peak_hour} with total sales of {peak_hour_sales}.")
