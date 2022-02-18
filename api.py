from typing import Dict

from fastapi import FastAPI
from fuel import Fuel
from fuel import Prices

app = FastAPI()
fuel = Fuel()


@app.get("/prices")
async def prices() -> Prices:
    return fuel.prices
