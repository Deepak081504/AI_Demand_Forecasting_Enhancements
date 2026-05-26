# app/notifications/app_notification.py
from sqlalchemy.orm import Session
from app.services.notification_service import create_app_notification

def dispatch_dashboard_alert(db: Session, user_id: str, text: str, status: str):
    create_app_notification(db, user_id, text, status)