from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TestResultCreate(BaseModel):
    user_id: Optional[int] = None
    test_id: int
    result_type: str  # CHAR(1)

class TestResultUpdate(BaseModel):
    result_type: Optional[str] = None

class TestResultResponse(BaseModel):
    test_result_id: int
    user_id: Optional[int]
    test_id: int
    result_type: str
    created_at: datetime

    class Config:
        from_attributes = True
