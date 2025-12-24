# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, create_access_token
from app.db.session import get_db
from app.db.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
