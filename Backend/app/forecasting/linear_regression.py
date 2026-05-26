# app/forecasting/linear_regression.py
import numpy as np
from sklearn.linear_model import LinearRegression

def run_linear_regression_prediction(series: list, steps: int):
    X = np.array(range(len(series))).reshape(-1, 1)
    y = np.array(series)
    model = LinearRegression().fit(X, y)
    
    future_X = np.array(range(len(series), len(series) + steps)).reshape(-1, 1)
    predictions = model.predict(future_X).tolist()
    
    fitted = model.predict(X)
    mae = float(np.mean(np.abs(y - fitted)))
    return predictions, mae