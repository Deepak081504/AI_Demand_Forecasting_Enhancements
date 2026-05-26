from pydantic import BaseModel


class DatasetBase(BaseModel):
    filename: str
    uploaded_by: str


class DatasetResponse(DatasetBase):
    id: int

    class Config:
        orm_mode = True