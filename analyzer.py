"""
File: analyzer.py
Author: SluG
Created: February 28, 2024
Description: HTML file parser
"""
import re
import requests

def extract_email_addresses(file_path):
    """
    Extract email addresses from a text file.

    Parameters:
    - file_path (str): The path to the text file.

    Returns:
    - list: A list of extracted email addresses.
    """
    logger.info("Start extract_email_addresses module")
    logger.info("Parameter file_path: " + file_path)
    email_addresses = []

    # Open the file and read its content
    with open(file_path, 'r') as file:
        content = file.read()

        # Use regular expression to find email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_addresses = re.findall(email_pattern, content)

    return email_addresses

    # Example usage:
    # file_path = 'path/to/your/text_file.txt'
    # result = extract_email_addresses(file_path)

    # if result:
    #     print("Extracted Email Addresses:")
    #     for email in result:
    #         print(email)
    # else:
    #     print("No email addresses found in the file.")
