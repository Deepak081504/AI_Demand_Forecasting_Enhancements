from pydantic import BaseModel


class ReportSchema(BaseModel):
    report_name: str
    report_path: str


class ReportResponse(ReportSchema):
    id: int

    class Config:
        orm_mode = True