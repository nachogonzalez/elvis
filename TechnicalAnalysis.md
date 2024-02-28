# ELVIS - Technical Analysis

## Modules
### Dyson
    - dyson.py
    - This module is the agent that gets the html files to analyze
### Analyzer
    - analyzer.py
    - HTML file parser
### DB Utils
    - dbutils.py
    - Module that provides tools to manage the different databases
## Workflows
### dyson.py
    1. Get the first link of LinksDB
    2. Get the html file
    3. Store the html file in /temp
    4. Call Analyzer
    5. Update LinksDB with the html analyzed
    6. Clean /temp
    7. Repeat
### analyzer.py
    1. Open the html file in /temp
    2. Parse the html file
    3. Update EmailsDB
## Databases
### LinksDB
#### links.xlsx
    - Tab: dashboard
        - totalNumber
    - Tab: links
        - link
        - dateAdded
        - processed
        - dateProcessed
### EmailsDB
#### emails.xlsx
    - Tab: dashboard
        - totalNumer
        - domainsNumber
    - Tab: emails
        - email
        - domain
        - dateAdded
