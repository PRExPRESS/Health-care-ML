import pandas as pd

try:
    # Read the CSV file
    dat = pd.read_csv('\dataset\Calorie_value.csv')
    # Print the first few rows of the dataframe
    print(dat.head())
except FileNotFoundError:
    print(f"The file was not found. Please check the file path: {dat}")
except pd.errors.EmptyDataError:
    print("The file is empty. Please provide a valid CSV file.")
except pd.errors.ParserError:
    print("There was an error parsing the file. Please check the file format.")