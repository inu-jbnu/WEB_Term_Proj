# app/routers/test.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.test import TestCreate, TestUpdate, TestResponse
from app.crud import test as crud_test
from app.db.session import get_db

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

@router.post("/", response_model=TestResponse)
def create_test(test_in: TestCreate, db: Session = Depends(get_db)):
    return crud_test.create_test(db, test_in)

@router.get("/{test_id}", response_model=TestResponse)
def read_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud_test.get_test(db, test_id)
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.get("/", response_model=list[TestResponse])
def read_tests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_test.get_tests(db, skip=skip, limit=limit)

@router.put("/{test_id}", response_model=TestResponse)
def update_test(test_id: int, test_in: TestUpdate, db: Session = Depends(get_db)):
    db_test = crud_test.update_test(db, test_id, test_in)
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.delete("/{test_id}", response_model=dict)
def delete_test(test_id: int, db: Session = Depends(get_db)):
    success = crud_test.delete_test(db, test_id)
    if not success:
        raise HTTPException(status_code=404, detail="Test not found")
    return {"ok": True}
