import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# PREPROCESS DATA
def preprocess_dataset(file_path):

    df = pd.read_csv(file_path)

    # REMOVE DUPLICATES
    df.drop_duplicates(inplace=True)

    # HANDLE NULL VALUES
    df.fillna(0, inplace=True)

    # CONVERT DATA TYPES
    df["Month"] = df["Month"].astype(int)
    df["Sales"] = df["Sales"].astype(float)

    # BASIC SUMMARY
    total_rows = len(df)
    total_sales = df["Sales"].sum()

    return {
        "message": "Dataset Preprocessed Successfully",
        "total_rows": total_rows,
        "total_sales": total_sales
    }


# GENERATE FORECAST
def generate_forecast(file_path):

    df = pd.read_csv(file_path)

    X = df[["Month"]]
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = 100 - mean_absolute_error(
        y_test,
        predictions
    )

    future_months = pd.DataFrame({
        "Month": [13, 14, 15, 16]
    })

    future_predictions = model.predict(
        future_months
    )

    return {
        "forecast": future_predictions.tolist(),
        "accuracy": round(accuracy, 2)
    }