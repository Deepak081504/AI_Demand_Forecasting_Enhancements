from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.notification import Notification

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# ADD NOTIFICATION
@router.post("/add")
def add_notification(
    message: str,
    db: Session = Depends(get_db)
):

    notification = Notification(
        message=message,
        status="unread"
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {
        "message": "Notification Added Successfully"
    }


# GET ALL NOTIFICATIONS
@router.get("/")
def get_notifications(
    db: Session = Depends(get_db)
):

    notifications = db.query(Notification).all()

    return {
        "total_notifications": len(notifications),
        "notifications": notifications
    }


# MARK AS READ
@router.put("/read/{notification_id}")
def mark_as_read(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        return {
            "error": "Notification Not Found"
        }

    notification.status = "read"

    db.commit()

    return {
        "message": "Notification Marked As Read"
    }


# MARK ALL NOTIFICATIONS AS READ
@router.put("/read-all")
def mark_all_notifications_read(
    db: Session = Depends(get_db)
):

    notifications = db.query(Notification).all()

    for notification in notifications:
        notification.status = "read"

    db.commit()

    return {
        "message": "All Notifications Marked As Read"
    }


# DELETE NOTIFICATION
@router.delete("/delete/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        return {
            "error": "Notification Not Found"
        }

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification Deleted Successfully"
    }