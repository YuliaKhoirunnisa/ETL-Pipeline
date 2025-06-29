import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from load import save_to_gsheet

class TestLoad(unittest.TestCase):

    @patch("load.gspread.authorize")
    def test_save_to_gsheet(self, mock_authorize):
        # Buat DataFrame dummy
        df = pd.DataFrame({
            "Title": ["T-shirt"],
            "Price": [160000],
            "Rating": [4.5],
            "Colors": [3],
            "Size": ["M"],
            "Gender": ["Unisex"],
            "timestamp": ["2025-06-02T00:00:00Z"]
        })

        # Mock koneksi gspread
        mock_client = MagicMock()
        mock_authorize.return_value = mock_client
        mock_spreadsheet = MagicMock()
        mock_client.open.return_value.worksheet.return_value = mock_spreadsheet

        # Jalankan function yang mau di-test
        save_to_gsheet(df, "TestSheet", creds_file="credentials.json")

        # Check kalau open spreadsheet berhasil dipanggil
        mock_client.open.assert_called_with("TestSheet")

        # Check kalau clear dan update dipanggil
        mock_spreadsheet.clear.assert_called_once()
        mock_spreadsheet.update.assert_called_once()

if __name__ == "__main__":
    unittest.main()