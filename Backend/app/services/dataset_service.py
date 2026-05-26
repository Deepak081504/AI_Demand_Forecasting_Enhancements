# app/services/dataset_service.py
from sqlalchemy.orm import Session
from app.models.dataset import DatasetMeta

def record_dataset_upload_meta(db: Session, filename: str, user: str):
    meta = DatasetMeta(filename=filename, uploaded_by=user)
    db.add(meta)
    db.commit()