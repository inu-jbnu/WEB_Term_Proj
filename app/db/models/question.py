from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("test.test_id"), nullable=False)
    content = Column(String(255), nullable=False)
    order_no = Column(Integer, nullable=False)

    test = relationship("Test", back_populates="questions")
    choices = relationship("QuestionChoice", back_populates="question")
    