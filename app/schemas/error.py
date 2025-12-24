from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class ErrorResponse(BaseModel):
    timestamp: datetime
    path: str
    status: int
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None
