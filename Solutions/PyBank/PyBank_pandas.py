# Imports
import os
import pandas as pd

# File path
csvpath = os.path.join('raw_data/budget_data_1.csv')
# csvpath = os.path.join('raw_data/budget_data_2.csv')

# Data frame creation
df = pd.read_csv(csvpath)
# df.head()

# Calculate total months
total_months = df['Date'].count()

# Calculate total revenue
total_revenue = df['Revenue'].sum()

# Create new column with revenue change
df['Revenue Change'] = df['Revenue'].diff()

# Calculate average revenue
average_revenue_change = df['Revenue Change'].mean()

# Finding rows of greatest increase and decrease
greatest_increase_row = df.iloc[df['Revenue Change'].idxmax()]
greatest_decrease_row = df.iloc[df['Revenue Change'].idxmin()]

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${average_revenue_change}\n"
    f"Greatest Increase in Revenue: {greatest_increase_row['Date']} "
    f"(${greatest_increase_row['Revenue Change']})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease_row['Date']} "
    f"(${greatest_decrease_row['Revenue Change']})\n")

# Print the output (to terminal)
print(output)
