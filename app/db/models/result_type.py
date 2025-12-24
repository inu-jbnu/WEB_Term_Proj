# app/db/models/result_type.py
from sqlalchemy import Column, CHAR, String, Text
from app.db.base import Base

class ResultType(Base):
    __tablename__ = "result_type"

    result_type = Column(CHAR(1), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    summary = Column(String(100))
