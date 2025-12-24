# app/db/models/question_choice.py
from sqlalchemy import Column, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.question import Question

class QuestionChoice(Base):
    __tablename__ = "question_choice"

    choice_id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    label = Column(CHAR(1), nullable=False)
    content = Column(String(255), nullable=False)
    result_type = Column(CHAR(1), nullable=False)

    question = relationship("Question", back_populates="choices")
