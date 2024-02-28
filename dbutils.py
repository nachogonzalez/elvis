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

def create_empty_excel_database(file_name):

    """
    Create an empty Excel database at the specified file path.

    Parameters:
    - file_path (str): The path where the Excel file will be saved.
    """

    logger.info("Start create_empty_excel module")

    # We create the workbook
    workbook = openpyxl.Workbook()

    # We get the active sheet
    sheet = workbook.active

    # We save the file
    workbook.save(file_name + ".xlsx")

    logger.info("Excel file created successfuly: " + file_name + ".xlsx")


def initializeDBs():
    """
    Initialize the databases

    Parameters:
    
    """
    logger.info("Start initializeDBs")
    linksDBname = "links"
    emailsDBname = "emails"
    create_empty_excel_database(linksDBname)
    logger.info("Links DB initialized")
    create_empty_excel_database(emailsDBname)
    logger.info("Emails DB initialized")
