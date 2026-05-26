from pydantic import BaseModel


class NotificationSchema(BaseModel):
    message: str
    status: str


class NotificationResponse(NotificationSchema):
    id: int

    class Config:
        orm_mode = True