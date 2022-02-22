import unittest
from datetime import date


import requests

from fuel import Fuel


class TestFuel(unittest.TestCase):
    def setUp(self) -> None:
        self.fuel = Fuel()
        self.number = 5

    def test_prices(self):
        self.assertIsInstance(self.fuel.prices, dict)
        self.number = 10

    def test_get_pdf_uri_path(self):
        res = requests.get(self.fuel._get_pdf_uri_path())
        self.assertEqual(res.status_code, 200)
        print(self.number)

    def test_extract_prices(self):
        prices = self.fuel._extract_prices(self.fuel._get_pdf_uri_path())
        self.assertIsInstance(prices, dict)
        self.number = 10

    def test_update_prices_cache(self):
        self.assertIsNone(self.fuel._update_prices_cache())
        self.assertEqual(self.fuel._last_cache_update, date.today())
        self.number = 10
