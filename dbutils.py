"""
File: dbutils.py
Author: SluG
Created: February 28, 2024
Description: Module that provides tools to manage the different databases
"""

import pandas as pd

def create_empty_excel_database(file_path):
    """
    Create an empty Excel database at the specified file path.

    Parameters:
    - file_path (str): The path where the Excel file will be saved.
    """
    # Create an empty DataFrame
    empty_df = pd.DataFrame()

    # Save the empty DataFrame to an Excel file
    empty_df.to_excel(file_path, index=False, engine='openpyxl')

    print(f"Empty Excel database created at: {file_path}")

def initializeDBs():
    file_path = '/temp/linksDB.xlsx'
    create_empty_excel_database(file_path)
