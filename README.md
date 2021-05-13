# XOLogParser
These are just some script to read your Crossout logs and make statistics for raids.

##How to run:
You need XORaidStatistics-empty.ods table.
###For csv output:
- Modify PVE_CSV.py. Replace those three strings with your own:
```
path = "/path/to/data/log"
name = "YourIngameName"
csv_file = '/tmp/test.csv'
```
- Run script PVE_CSV.py
- Open test.csv in Excel or Calc and copy those two parts to appropriate place in XORaidStatistics-empty.ods

###For Google Sheets output:
There are a few complications with running PVE.py and letting it write directly to your Google Sheets.
- To modify Google sheet documents you need credentials.json - described in the documentation: https://developers.google.com/sheets/api/quickstart/python
- Get credentials.json and copy it to same folder as other scripts
- You need some python modules - you have to install it with PIp
    - https://pypi.org/project/google-auth-oauthlib/
    - https://pypi.org/project/google-api-python-client/
    - https://google-auth.readthedocs.io/en/latest/index.html
    - *TODO: Use only one of them, they have duplicate functions...*
- Import XORaidStatistics-empty.ods to your Google Drive and write down its ID.
- Modify PVE.py. Replace those three strings with your own:
```
path = "/path/to/data/log"
name = "YourIngameName"
SPREADSHEET_ID = 'yourGoogleSpreadSheetsCopyOfTableIDIDIDIDID0'
```
- For the first run it should write web link to console - open that link and allow access to your Google Drive.
- For the second run it should write directly to your document.

### TODO: 
R scripts for further analysis...
