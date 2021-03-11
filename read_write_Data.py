from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file']


# The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = '1TZHBYfwbXrFOCIVXUu_dwR38obeJpWjDzE8s0ern5Xg'
SHEET_NAME = 'Raid'
DATA_TOP_LEFT = 'A21'
DATA_TOP_LEFT_PRICE = 'D3'
DATA_RIGHT = "M"
DATA_BOTTOM_RIGHT = "M10000000"


def read_google_sheet(spreadsheet_id):
    return _google_sheet(spreadsheet_id=spreadsheet_id, operation="Read_Raid_Data")


def write_google_sheet(spreadsheet_id, data):
    return _google_sheet(spreadsheet_id=spreadsheet_id, operation="Write_Raid_Data", data=data)


def write_google_sheet_price(spreadsheet_id, data):
    return _google_sheet(spreadsheet_id=spreadsheet_id, operation="Write_Price", data=data)


def _google_sheet(spreadsheet_id, operation, data=None):
    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()

    if operation == "Read_Raid_Data":
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=SHEET_NAME+'!'+DATA_TOP_LEFT+':'+DATA_RIGHT).execute()

        return result.get('values', [])

    elif operation == "Write_Raid_Data":
        value_range_body = {
            'majorDimension': 'ROWS',
            'values': data
        }
        # TODO: check result
        result = sheet.values().clear(spreadsheetId=spreadsheet_id,
                                       range=SHEET_NAME+'!'+DATA_TOP_LEFT+':'+DATA_BOTTOM_RIGHT).execute()

        result = sheet.values().update(spreadsheetId=spreadsheet_id,
                                       range=SHEET_NAME+'!'+DATA_TOP_LEFT,
                                       valueInputOption='RAW',
                                       body=value_range_body).execute()

    elif operation == "Write_Price":
        value_range_body = {
            'majorDimension': 'ROWS',
            'values': data
        }
        # TODO: check result
        result = sheet.values().update(spreadsheetId=spreadsheet_id,
                                       range=SHEET_NAME+'!'+DATA_TOP_LEFT_PRICE,
                                       valueInputOption='RAW',
                                       body=value_range_body).execute()