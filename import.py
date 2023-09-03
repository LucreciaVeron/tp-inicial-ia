import pandas as pd
import random

# Load your dataset into a DataFrame (replace 'your_dataset.csv' with your dataset file)
df = pd.read_csv('Covid19Casos.csv')

# Check if the dataset has at least 15,000 unique rows; if not, use the current number of unique rows
num_rows_to_select = min(10000, len(df))

# Generate a list of unique random row indices
random_indices = random.sample(range(len(df)), num_rows_to_select)

# Select the rows with the randomly generated indices
random_sample = df.iloc[random_indices]

# If you want to save the random sample to a new CSV file, you can use:
random_sample.to_csv('./Datos/random_sample.csv', index=False)