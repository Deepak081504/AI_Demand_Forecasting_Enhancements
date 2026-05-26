def run_random_forest_prediction(series: list, steps: int):
    return [val * 1.02 for val in series[-steps:]], 5.2