import read_write_Google
import parse_PVE
import parse_XCODB

path = "/path/to/data/log"
name = "YourIngameName"
SPREADSHEET_ID = 'yourGoogleSpreadSheetsCopyOfTableIDIDIDIDID0'

# Read previous data from google sheet
data = read_write_Google.read_google_sheet(spreadsheet_id=SPREADSHEET_ID)

# Read new data from logs
data_updated = parse_PVE.read(path, name, data)

# Write to google docs
read_write_Google.write_google_sheet(spreadsheet_id=SPREADSHEET_ID, data=data_updated)

# Read prices from https://crossoutdb.com/
data_price = parse_XCODB.read()

# Write to google docs
read_write_Google.write_google_sheet_price(spreadsheet_id=SPREADSHEET_ID, data=data_price)

# input("Press anything to exit...")
