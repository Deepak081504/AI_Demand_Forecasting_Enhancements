from sqlalchemy import Column, Integer, String
from app.database import Base


class Notification(Base):

    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    message = Column(String(255))

    status = Column(String(50), default="unread")