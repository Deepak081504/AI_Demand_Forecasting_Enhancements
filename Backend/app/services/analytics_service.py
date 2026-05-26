import pandas as pd


def dashboard_analytics(file_path):
    df = pd.read_csv(file_path)

    total_sales = df["Sales"].sum()
    average_sales = df["Sales"].mean()
    top_product = df.groupby("Product")["Sales"].sum().idxmax()

    return {
        "total_sales": total_sales,
        "average_sales": average_sales,
        "top_product": top_product
    }