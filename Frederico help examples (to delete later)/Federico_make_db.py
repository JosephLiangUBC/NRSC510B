import pandas as pd
import sqlite3
from sqlite3 import IntegrityError


# Load the CSV file into a DataFrame
csv_file_path = 'tap_output.csv'
df = pd.read_csv(csv_file_path)


# Function for basic data validation
def validate_data(df):
    # Define expected data types
    expected_dtypes = {
        'Unnamed: 0': 'int64',
        'time': 'float64',
        'dura': 'float64',
        'dist': 'float64',
        'prob': 'float64',
        'speed': 'float64',
        'plate': 'int64',
        'taps': 'float64',
        'dataset': 'object',
        'Gene': 'object',
        'Allele': 'object'
    }
    
    # Type validation
    for col, expected_dtype in expected_dtypes.items():
        if df[col].dtype != expected_dtype:
            return False, f"Column {col} has incorrect data type {df[col].dtype}. Expected {expected_dtype}."
    
    # Range validation for specific columns
    if df['prob'].min() < 0 or df['prob'].max() > 1:
        return False, "Column 'prob' has values outside the range [0, 1]."
    
    return True, "Data is valid."

# Validate the data
is_valid, validation_message = validate_data(df)
if is_valid:
    # Create SQLite database and insert data
    try:
        conn = sqlite3.connect('c_elegans_data.db')
        df.to_sql('experiment_data', conn, if_exists='replace', index=False)
        etl_status = "Data successfully inserted into SQLite database."
    except IntegrityError as e:
        etl_status = f"Data insertion failed: {e}"
else:
    etl_status = f"Data validation failed: {validation_message}"

print(etl_status)
