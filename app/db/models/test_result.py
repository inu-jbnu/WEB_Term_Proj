# app/db/models/test_result.py
from sqlalchemy import Column, Integer, ForeignKey, CHAR, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.user import User
from app.db.models.test import Test

class TestResult(Base):
    __tablename__ = "test_result"

    test_result_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=True)
    test_id = Column(Integer, ForeignKey("test.test_id"), nullable=False)
    result_type = Column(CHAR(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="test_results")
    test = relationship("Test")
    answers = relationship("Answer", back_populates="test_result")
