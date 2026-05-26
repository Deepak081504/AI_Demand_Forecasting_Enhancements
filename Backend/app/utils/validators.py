# app/utils/validators.py
from fastapi import HTTPException

def validate_historical_data_bounds(values: list):
    if not values or len(values) < 3:
        raise HTTPException(status_code=400, detail="Insufficient data element length criteria failed.")