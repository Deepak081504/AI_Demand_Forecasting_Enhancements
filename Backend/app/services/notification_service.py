# app/services/notification_service.py
from sqlalchemy.orm import Session
from app.models.notification import NotificationRecord

def create_app_notification(db: Session, user_id: str, message: str, notif_type: str):
    notif = NotificationRecord(user_id=user_id, message=message, type=notif_type)
    db.add(notif)
    db.commit()