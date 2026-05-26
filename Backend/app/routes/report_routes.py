from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.report_service import (
    export_pdf,
    export_excel
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# EXPORT PDF
@router.get("/export/pdf")
def export_report_pdf():

    file_path = export_pdf()

    return FileResponse(
        path=file_path,
        filename="forecast_report.pdf",
        media_type="application/pdf"
    )


# EXPORT EXCEL
@router.get("/export/excel")
def export_report_excel():

    file_path = export_excel()

    return FileResponse(
        path=file_path,
        filename="forecast_report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )