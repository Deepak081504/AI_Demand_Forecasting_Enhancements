from pydantic import BaseModel
from typing import List


class ForecastRequest(BaseModel):
    month: int


class ForecastResponse(BaseModel):
    forecast: List[float]