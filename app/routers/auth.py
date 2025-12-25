# app/routers/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, create_access_token
from app.db.session import get_db
from app.db.models.user import User
from app.core.error_codes import USER_NOT_FOUND, UNAUTHORIZED
from app.core.exception import AppException

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise AppException(**USER_NOT_FOUND, details={"email": data.email})
    if not verify_password(data.password, user.password):
        raise AppException(**UNAUTHORIZED, details={"email": data.email})
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
