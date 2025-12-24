from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# SQLAlchemy 엔진 생성
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스
Base = declarative_base()

# Dependency: DB 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
