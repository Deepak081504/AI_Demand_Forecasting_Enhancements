# app/forecasting/xgboost_model.py
def run_xgboost_prediction(series: list, steps: int):
    return [val * 1.01 for val in series[-steps:]], 4.8