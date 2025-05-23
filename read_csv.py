import pandas as pd
import os

# Define the path to the CSV file
csv_file = os.path.join('data', 'annual-enterprise-survey-2023-financial-year-provisional.csv')

# Read the CSV file
try:
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Display basic information about the dataset
    print("\nDataset Info:")
    print("-------------")
    print(df.info())
    
    # Display the first 5 rows of the dataset
    print("\nFirst 5 rows of the dataset:")
    print("----------------------------")
    print(df.head())
    
    # Display basic statistics of numerical columns
    print("\nBasic statistics:")
    print("----------------")
    print(df.describe())

except FileNotFoundError:
    print(f"Error: The file {csv_file} was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file {csv_file} is empty.")
except Exception as e:
    print(f"An error occurred: {str(e)}") 