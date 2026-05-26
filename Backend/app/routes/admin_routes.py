from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User
from app.models.dataset import Dataset
from app.models.forecast import Forecast
from app.models.notification import Notification

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# ADMIN DASHBOARD
@router.get("/dashboard")
def admin_dashboard(
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()
    total_datasets = db.query(Dataset).count()
    total_forecasts = db.query(Forecast).count()
    total_notifications = db.query(Notification).count()

    return {
        "total_users": total_users,
        "total_datasets": total_datasets,
        "total_forecasts": total_forecasts,
        "total_notifications": total_notifications
    }


# LIST USERS
@router.get("/users")
def list_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()

    return {
        "total_users": len(users),
        "users": users
    }


# DELETE USER
@router.delete("/delete-user/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return {
            "error": "User Not Found"
        }

    db.delete(user)
    db.commit()

    return {
        "message": "User Deleted Successfully"
    }


# LIST ALL DATASETS
@router.get("/datasets")
def list_all_datasets(
    db: Session = Depends(get_db)
):

    datasets = db.query(Dataset).all()

    return {
        "total_datasets": len(datasets),
        "datasets": datasets
    }


# LIST ALL FORECASTS
@router.get("/forecasts")
def list_all_forecasts(
    db: Session = Depends(get_db)
):

    forecasts = db.query(Forecast).all()

    return {
        "total_forecasts": len(forecasts),
        "forecasts": forecasts
    }


# LIST ACTIVITIES
@router.get("/activities")
def list_activities(
    db: Session = Depends(get_db)
):

    users = db.query(User).count()
    datasets = db.query(Dataset).count()
    forecasts = db.query(Forecast).count()

    activities = [
        f"{users} Users Registered",
        f"{datasets} Datasets Uploaded",
        f"{forecasts} Forecasts Generated"
    ]

    return {
        "activities": activities
    }