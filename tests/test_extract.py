import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import scrape_page
import unittest

class TestExtract(unittest.TestCase):
    def test_scrape_page_returns_list(self):
        data = scrape_page(1)
        self.assertIsInstance(data, list)
        if data:
            self.assertIn("Title", data[0])
            self.assertIn("Price", data[0])

if __name__ == "__main__":
    unittest.main()