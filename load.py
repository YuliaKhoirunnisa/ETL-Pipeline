import os
import gspread
from google.oauth2.service_account import Credentials

def save_to_csv(df, filename="fashion_studio_data.csv"):
    try:
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)
        df.to_csv(filename, index=False)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving file {filename}: {e}")

def save_to_gsheet(df, spreadsheet_name, worksheet_name="Sheet1", creds_file="credentials.json"):
    try:
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file(creds_file, scopes=scopes)
        client = gspread.authorize(creds)

        try:
            sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            sheet = client.open(spreadsheet_name).add_worksheet(title=worksheet_name, rows="1000", cols="20")

        sheet.clear()

        # 🔥 FIX untuk error NaN:
        df = df.fillna("")  # menggantikan NaN dengan string kosong agar JSON valid

        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        print(f"✅ Data berhasil dikirim ke Google Sheet: {spreadsheet_name}")
    except Exception as e:
        print(f"❌ Error menyimpan ke Google Sheets: {e}")