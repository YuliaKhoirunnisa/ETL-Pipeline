import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from transform import (
    convert_price_to_idr,
    clean_rating,
    extract_number_colors,
    clean_size,
    clean_gender,
    transform_data,
    remove_invalid_data
)

class TestTransform(unittest.TestCase):

    def test_convert_price_to_idr(self):
        self.assertEqual(convert_price_to_idr("$10.00"), 160000)
        self.assertIsNone(convert_price_to_idr("invalid"))

    def test_clean_rating(self):
        self.assertEqual(clean_rating("Rating: ⭐ 4.8 / 5"), 4.8)
        self.assertIsNone(clean_rating("no rating"))

    def test_extract_number_colors(self):
        self.assertEqual(extract_number_colors("3 colors"), 3)
        self.assertIsNone(extract_number_colors("Colorful"))

    def test_clean_size(self):
        self.assertEqual(clean_size("Size: M"), "M")

    def test_clean_gender(self):
        self.assertEqual(clean_gender("Gender: Male"), "Male")

    def test_transform_data_removes_duplicates(self):
        duplicate_data = [
            {"Title": "T-shirt", "Price": "$10.00", "Rating": "Rating: ⭐ 4.5 / 5", "Colors": "3 colors", "Size": "Size: M", "Gender": "Gender: Unisex", "timestamp": "2025-06-02T00:00:00Z"},
            {"Title": "T-shirt", "Price": "$10.00", "Rating": "Rating: ⭐ 4.5 / 5", "Colors": "3 colors", "Size": "Size: M", "Gender": "Gender: Unisex", "timestamp": "2025-06-02T00:00:00Z"}  # Duplicate
        ]

        df = transform_data(duplicate_data)

        self.assertEqual(len(df), 1)  # Harusnya cuma 1 setelah drop_duplicates

    def test_remove_invalid_data(self):
        dirty_data = [
            {"Title": "Unknown Product", "Price": "$10.00", "Rating": "Rating: ⭐ 5 / 5", "Colors": "2 colors", "Size": "Size: M", "Gender": "Gender: Unisex", "timestamp": "2025-06-02T00:00:00Z"},
            {"Title": "Valid Product", "Price": "$10.00", "Rating": "Rating: ⭐ 4.5 / 5", "Colors": "3 colors", "Size": "Size: L", "Gender": "Gender: Male", "timestamp": "2025-06-02T00:00:00Z"},
            {"Title": "Valid Product", "Price": None, "Rating": "Rating: ⭐ 4.8 / 5", "Colors": "5 colors", "Size": "Size: S", "Gender": "Gender: Female", "timestamp": "2025-06-02T00:00:00Z"}
        ]

        df = transform_data(dirty_data)
        df_cleaned = remove_invalid_data(df)

        self.assertNotIn("Unknown Product", df_cleaned["Title"].values)
        self.assertFalse(df_cleaned["Price"].isna().any())
        self.assertFalse(df_cleaned["Rating"].isna().any())

if __name__ == "__main__":
    unittest.main()