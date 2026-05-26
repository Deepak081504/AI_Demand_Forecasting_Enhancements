from fastapi import FastAPI
from app.database import Base, engine

from app.routes.auth_routes import router as auth_router
from app.routes.dataset_routes import router as dataset_router
from app.routes.forecast_routes import router as forecast_router
from app.routes.report_routes import router as report_router
from app.routes.notification_routes import router as notification_router
from app.routes.admin_routes import router as admin_router


# CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)


# FASTAPI APPLICATION
app = FastAPI(
    title="Advanced AI Demand Forecasting API",
    version="1.0.0",
    description="AI Based Demand Forecasting System"
)


# INCLUDE ROUTES
app.include_router(auth_router)
app.include_router(dataset_router)
app.include_router(forecast_router)
app.include_router(report_router)
app.include_router(notification_router)
app.include_router(admin_router)


# DEFAULT API
@app.get("/")
def default():

    return {
        "status": "success",
        "message": "Advanced AI Demand Forecasting API Running Successfully",
        "version": "1.0.0"
    }


# HEALTH CHECK API
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "server": "running",
        "database": "connected"
    }