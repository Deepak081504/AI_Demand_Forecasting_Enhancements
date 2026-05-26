from fastapi import APIRouter

from app.services.forecasting_service import (
    preprocess_dataset,
    generate_forecast
)

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


# PREPROCESS DATA
@router.get("/preprocess")
def preprocess_data():

    file_path = "app/uploads/sales.csv"

    result = preprocess_dataset(file_path)

    return result


# GENERATE FORECAST
@router.get("/generate")
def generate_forecast_api():

    file_path = "app/uploads/sales.csv"

    result = generate_forecast(file_path)

    return result