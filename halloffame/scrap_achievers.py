from __future__ import print_function
import pandas as pd
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import matplotlib.pyplot as plt


def get_data():
    secret_df = pd.read_csv('CONFIDENTIAL')
    ID = secret_df.iloc[0, 0]
    SHEET_NAME = secret_df.iloc[3, 0]

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

    data = []
    slack_mentioned_message = ""
    # comments = ""
    if not values:
        print('No data found.')
    else:
        print('DATA FOUND !!')
        with open('comments.txt', 'w') as file:
            for row in values:
                # Print rows A and E, which correspond to indices 0 and 4.
                try:
                    if len(row) == 6:
                        data.append([row[0], row[1], row[2], row[3], row[4], row[5]])
                    else:
                        data.append([row[0], row[1], row[2], row[3], row[4], ''])
                    slack_mentioned_message += "@"+str(row[3]+",\n")
                    file.write("{}\n".format(row[5]))
                except Exception as err:
                    print(err)


    df = pd.DataFrame(data, columns =['date', 'email', 'name', 'slack_name', 'iscomplete', 'comment'])

    df.to_csv('achievers.csv', index=False)
    return df

# df = pd.read_csv('achievers.csv')
df = get_data()
print(df.head())

print(df.shape)
print("========")
# print(slack_mentioned_message)

df['date'] = pd.to_datetime(df.date)
df['date'] = df['date'].dt.strftime('%d/%m/%y')

print(df.head())

#filter duplicates
duplicateRowsDF = df[df.duplicated(['slack_name'])]

print(duplicateRowsDF['slack_name'])

df = df.drop(index=duplicateRowsDF.index)

print(df.shape)

df = df['date'].value_counts()

# df = df.reindex(columns=['date', 'Achievers'])

print(df)
df.plot(kind='bar', figsize=(40, 10), color='#02b3e4', rot=0, width=0.7, align='center')

plt.title("HONORABLE MENTIONS WALL| 50 Days of Udacity")

plt.xlabel("Date", labelpad=5)
plt.ylabel("Achievers", labelpad=5)

FIG_NAME = 'achievers.png'

plt.savefig(FIG_NAME, dpi=50, bbox_inches='tight')
plt.show()
