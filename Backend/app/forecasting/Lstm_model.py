def run_lstm_prediction(series: list, steps: int):
    return [val * 0.99 for val in series[-steps:]], 6.1