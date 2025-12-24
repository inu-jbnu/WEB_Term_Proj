from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.db.models.user import User
from app.db.session import get_db
from app.core.security import hash_password

from app.core.error_codes import USER_NOT_FOUND
from app.core.exception import AppException




router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# 전체 사용자 조회
@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 사용자 생성
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        email=user.email,
        password=hash_password(user.password),
        nickname=user.nickname
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 특정 사용자 조회
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        # AppException 사용
        raise AppException(**USER_NOT_FOUND, details={"user_id": user_id})
    return user

