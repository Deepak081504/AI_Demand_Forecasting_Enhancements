# app/forecasting/model_comparison.py
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from app.forecasting.linear_regression import run_linear_regression_prediction

def evaluate_best_forecasting_model(series: list, steps: int):
    """Multiple model evaluation matrix framework using minimum Mean Absolute Error (MAE)"""
    lr_preds, lr_mae = run_linear_regression_prediction(series, steps)
    
    try:
        arima_model = ARIMA(series, order=(1, 1, 0))
        arima_fit = arima_model.fit()
        arima_preds = arima_fit.forecast(steps=steps).tolist()
        arima_mae = float(np.mean(np.abs(np.array(series) - arima_fit.fittedvalues)))
    except Exception:
        arima_preds, arima_mae = lr_preds, lr_mae + 10.0 # Error isolation fallback
        
    if arima_mae <= lr_mae:
        return "ARIMA", arima_preds, arima_mae
    return "LinearRegression", lr_preds, lr_mae