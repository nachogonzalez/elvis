"""
File: dbutils.py
Author: SluG
Created: February 28, 2024
Description: Module that provides tools to manage the different databases
"""

import pandas as pd
import os
from loguru import logger
import openpyxl

def excel_file_exists(file_path):
    """
    Check if an Excel file exists at the given file path.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    logger.info("Start excel_file_exists")
    logger.info("Parameter file_path: " + file_path)
    return os.path.isfile(file_path)


def create_empty_excel_database(file_name):
    """
    Create an empty Excel database at the specified file path.

    Parameters:
    - file_path (str): The path where the Excel file will be saved.
    """
    logger.info("Start create_empty_excel module")
    logger.info("Parameter file_name: " + file_name)
    file_path = file_name

    if excel_file_exists(file_name):        
        logger.info("The Excel file " + file_name + " exists, so we don't create it again.")
    else:
        logger.info("The Excel file " + file_name + " does not exist, so we create it.")
        # We create the workbook
        workbook = openpyxl.Workbook()
        # We get the active sheet
        sheet = workbook.active
        # We save the file
        workbook.save(file_name)
        logger.info("Excel file created successfuly: " + file_name)

def initializeDBs():
    """
    Initialize the databases

    Parameters:
    
    """
    logger.info("Start initializeDBs")
    # Definition of the databases names
    linksDBname = "links.xlsx"
    emailsDBname = "emails.xlsx"
    # Check that databases exist. If not, is the first time we run the agent, so we create them
    create_empty_excel_database(linksDBname)
    logger.info("Links DB initialized")
    create_empty_excel_database(emailsDBname)
    logger.info("Emails DB initialized")
