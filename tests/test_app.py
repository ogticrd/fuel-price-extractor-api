

from api import app
from fastapi.testclient import TestClient
import unittest
import sys
from os.path import abspath, dirname, join
sys.path.insert(1, abspath(join(dirname(dirname(__file__)), 'src')))


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_prices(self):
        res = self.client.get('/prices')
        self.assertEqual(res.status_code, 200)
