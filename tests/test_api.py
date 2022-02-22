from fastapi.testclient import TestClient
import unittest

from api import app


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_prices(self):
        res = self.client.get('/prices')
        self.assertEqual(res.status_code, 200)
