# google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use credentials to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def get_gspread_client():
    creds = ServiceAccountCredentials.8466ac210cb15d6da2801ff688fc0c98e28be812('credentials.json', scope)
    client = gspread.authorize(creds)
    return client

def get_worksheet(sheet_name, worksheet_name):
    client = get_gspread_client()
    sheet = client.open(sheet_name)
    return sheet.worksheet(worksheet_name)

def get_all_records(sheet_name, worksheet_name):
    worksheet = get_worksheet(sheet_name, worksheet_name)
    return worksheet.get_all_records()

def append_row(sheet_name, worksheet_name, row):
    worksheet = get_worksheet(sheet_name, worksheet_name)
    worksheet.append_row(row)
