# XOLogParser
These are just some script to read your Crossout logs and make statistics for raids.

##How to run:
You need XORaidStatistics-empty.ods table.
###For csv output:
- Modify PVE_CSV.py. Replace those three strings with your own:
```
# Mind the slashes - you have to use forward slash or two backslashes
path = "C:/Users/John/Documents/My Games/Crossout/logs/"
name = "YourIngameName"
csv_file = 'C:\\Users\\John\\Desktop\\test.csv'
```
- Run script PVE_CSV.py
- Open test.csv in Excel or Calc and copy those two parts to appropriate place in XORaidStatistics-empty.ods

###For Google Sheets output:
There are a few complications with running PVE.py and letting it write directly to your Google Sheets.
- To modify Google sheet documents you need credentials.json - described in the documentation: https://developers.google.com/sheets/api/quickstart/python
- Get credentials.json and copy it to same folder as other scripts
- You need some python modules - you have to install it with PIp
    - https://pypi.org/project/google-auth-oauthlib/
      - pip install --upgrade google-auth-oauthlib
    - https://pypi.org/project/google-api-python-client/
      - pip install --upgrade google-api-python-client
    - *TODO: Use only one of them, they probably have duplicate functions...*
- Create empty Google Spreadsheet and File -> Import XORaidStatistics-empty.ods
- Modify PVE.py. Replace those three strings with your own:
```
# Mind the slashes - you have to use forward slash or two backslashes
path = "C:/Users/John/Documents/My Games/Crossout/logs/"
name = "YourIngameName"
SPREADSHEET_ID = 'yourGoogleSpreadSheetsCopyOfTableIDIDIDIDID0'
```
- For the first run it should write web link to console - open that link and allow access to your Google Drive.
- For the second run it should write directly to your document.
###Automaticly run this script before launching Crossout:
Create .bat file with something similar

**(Mind the slashes, you have to use single backslash here)**
```
cd C:\Users\John\Desktop\XOLogParser
C:\Python-3.8.6\python.exe C:\Users\John\Desktop\XOLogParser\PVE.py
cd C:\Users\John\AppData\Local\Crossout
start launcher.exe

exit
```
### TODO: 
R scripts for further analysis...
