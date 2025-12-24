# app/schemas/auth.py
from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="user@example.com", description="로그인 이메일")
    password: str = Field(..., min_length=8, max_length=100, example="password123!", description="비밀번호")
