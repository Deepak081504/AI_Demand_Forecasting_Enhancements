from sqlalchemy import Column, Integer, String
from app.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    report_name = Column(String(255))
    report_path = Column(String(255))