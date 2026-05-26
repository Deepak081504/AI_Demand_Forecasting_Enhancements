import pandas as pd
from fpdf import FPDF


# EXPORT PDF
def export_pdf():

    data = {
        "Month": [1, 2, 3, 4],
        "Sales": [100, 200, 300, 400]
    }

    df = pd.DataFrame(data)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Forecast Report", ln=True)

    for index, row in df.iterrows():

        text = f"Month : {row['Month']}  Sales : {row['Sales']}"

        pdf.cell(200, 10, txt=text, ln=True)

    file_path = "forecast_report.pdf"

    pdf.output(file_path)

    return file_path


# EXPORT EXCEL
def export_excel():

    data = {
        "Month": [1, 2, 3, 4],
        "Sales": [100, 200, 300, 400]
    }

    df = pd.DataFrame(data)

    file_path = "forecast_report.xlsx"

    df.to_excel(
        file_path,
        index=False
    )

    return file_path