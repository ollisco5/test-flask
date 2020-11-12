from oauth2client.service_account import ServiceAccountCredentials

import gspread as gs

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gspread_creds = gs.authorize(creds)

sheet = gspread_creds.open("Inlämningsuppgift 7").sheet1



with open("values.txt", "r") as file:
    values = file.read().split("\n")
    values.remove("")
    print(values)
    row = 2
    col = 1
    for val in values:
        sheet.update_cell(row, col, float(val))
        row += 1

