# app/services/auth_service.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

def create_platform_user(db: Session, schema: UserCreate):
    dummy_hashed = schema.password + "hashed" # Production systems use passlib
    db_user = User(username=schema.username, hashed_password=dummy_hashed, role=schema.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user