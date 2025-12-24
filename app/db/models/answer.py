# app/db/models/answer.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.test_result import TestResult
from app.db.models.question import Question
from app.db.models.question_choice import QuestionChoice

class Answer(Base):
    __tablename__ = "answer"

    answer_id = Column(Integer, primary_key=True, index=True)
    test_result_id = Column(Integer, ForeignKey("test_result.test_result_id"), nullable=False)
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    choice_id = Column(Integer, ForeignKey("question_choice.choice_id"), nullable=False)

    test_result = relationship("TestResult", back_populates="answers")
    question = relationship("Question")
    choice = relationship("QuestionChoice")
