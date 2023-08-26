# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:02:41 2023

@author: Nacho
"""
import pandas as pd

# Load the entire dataset
# Replace 'your_dataset.csv' with the actual file name and path
df = pd.read_csv('Covid19Casos.csv')

# Extract the first 15000 rows
subset_df = df.head(15000)

# Save the extracted subset to a new CSV file
# Replace 'subset_output.csv' with the desired output file name and path
subset_df.to_csv('subset_output.csv', index=False)

print("Subset saved to 'subset_output.csv'")
