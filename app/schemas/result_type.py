from pydantic import BaseModel
from typing import Optional

class ResultTypeCreate(BaseModel):
    result_type: str  # CHAR(1)
    name: str
    description: Optional[str] = None
    summary: Optional[str] = None

class ResultTypeUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    summary: Optional[str] = None

class ResultTypeResponse(BaseModel):
    result_type: str
    name: str
    description: Optional[str] = None
    summary: Optional[str] = None

    class Config:
        from_attributes = True
