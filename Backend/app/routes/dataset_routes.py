import os
import pandas as pd

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dataset import Dataset

router = APIRouter(
    prefix="/dataset",
    tags=["Dataset"]
)

UPLOAD_FOLDER = "app/uploads"


# Upload Dataset
@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)

    new_dataset = Dataset(
        filename=file.filename,
        uploaded_by="admin"
    )

    db.add(new_dataset)
    db.commit()
    db.refresh(new_dataset)

    return {
        "message": "Dataset Uploaded Successfully",
        "rows": len(df),
        "filename": file.filename
    }


# GET ALL DATASETS
@router.get("/list")
def get_all_datasets(
    db: Session = Depends(get_db)
):

    datasets = db.query(Dataset).all()

    return {
        "total_datasets": len(datasets),
        "datasets": datasets
    }


# LIST USER DATASETS
@router.get("/user/{username}")
def list_user_datasets(
    username: str,
    db: Session = Depends(get_db)
):

    datasets = db.query(Dataset).filter(
        Dataset.uploaded_by == username
    ).all()

    return {
        "username": username,
        "datasets": datasets
    }


# SEARCH DATASET
@router.get("/search")
def search_dataset(
    filename: str,
    db: Session = Depends(get_db)
):

    datasets = db.query(Dataset).filter(
        Dataset.filename.like(f"%{filename}%")
    ).all()

    return {
        "search": filename,
        "results": datasets
    }



