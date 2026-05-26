from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    predicted_sales = Column(Float)
    accuracy = Column(Float)