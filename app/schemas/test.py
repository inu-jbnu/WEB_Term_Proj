# app/schemas/test.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TestBase(BaseModel):
    title: str
    description: Optional[str] = None

class TestCreate(TestBase):
    pass

class TestUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class TestResponse(TestBase):
    test_id: int
    created_at: datetime

    class Config:
        from_attributes = True
