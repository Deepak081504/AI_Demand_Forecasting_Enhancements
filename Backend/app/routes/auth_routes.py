from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, LoginSchema
from app.auth.password_handler import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "Invalid Email"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid Password"}

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }