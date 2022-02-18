from typing import Optional
from typing import Dict

from datetime import date
import json

from bs4 import BeautifulSoup
import requests
import tabula

Prices = Optional[Dict[str, float]]


class Fuel():
    _prices: Prices
    _last_cache_update: Optional[date]

    def __init__(self) -> None:
        self._prices = None
        self._last_cache_update = None
        self._micm_history_fuel_price_url = "https://micm.gob.do/direcciones/combustibles/avisos-semanales-de-precios/aviso-semanal-de-precios-de-combustibles-version-12-11-2021"
        self._update_prices_cache()

    def _get_pdf_uri_path(self) -> str:
        page = requests.get(self._micm_history_fuel_price_url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all(class_="yoo-zoo element-download-button")
        return f"https://micm.gob.do{results[0]['href']}"

    def _extract_prices(self, pdf_uri_path: str) -> Prices:
        df = tabula.read_pdf(pdf_uri_path)[0]

        df = df.rename(columns={'Unnamed: 0': 'type', 'Unnamed: 3': 'price'})
        df = df[['type', 'price']].dropna()

        result = df.to_json(orient="table")
        parsed = json.loads(result)

        prices = {}
        for p in parsed['data']:
            if "Gas Licuado de Petr\u00f3leo (GLP) **" == p['type']:
                prices[p['type']] = p['price'][5:]  # eye
                continue

            prices[p['type']] = p['price']

        return prices

    def _update_prices_cache(self) -> None:
        if not self._prices or not self._last_cache_update or self._last_cache_update > date.today():
            pdf_uri_path = self._get_pdf_uri_path()
            self._prices = self._extract_prices(pdf_uri_path)
            self._last_cache_update = date.today()

    @property
    def prices(self) -> Prices:
        self._update_prices_cache()
        return self._prices
