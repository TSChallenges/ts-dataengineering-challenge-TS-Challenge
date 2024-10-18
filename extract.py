# data_engineering/extract.py

import pandas as pd

def extract_data(file_path):
    """
    Extracts data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Extracted data.
    """
    df = pd.read_csv(file_path)

    return df


