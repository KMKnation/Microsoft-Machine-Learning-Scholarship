from __future__ import print_function
import pandas as pd
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

secret_df = pd.read_csv('CONFIDENTIAL')
ID = secret_df.iloc[0, 0]
SHEET_NAME = secret_df.iloc[2, 0]

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ID
SAMPLE_RANGE_NAME = SHEET_NAME + '!A3:Q'

"""Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

students = []
if not values:
    print('No data found.')
else:
    print('DATA FOUND !!')
    for row in values:
        # Print rows A and E, which correspond to indices 0 and 4.
        print('%s, %s, %s, %s, %s, %s, %s, %s, %s' % (row[0], row[2], row[4], row[6], row[8], row[10], row[12], row[14], row[16]))
        try:
            for col in range(len(row)):
                if col in [0.4, 6, 8, 10, 12, 14, 16]:
                    students.append(row[col])
        except Exception as err:
            print(err)

print(len(students))
