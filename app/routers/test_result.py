from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.deps import get_db
from app.crud import test_result as crud
from app.schemas.test_result import TestResultCreate, TestResultUpdate, TestResultResponse

router = APIRouter(prefix="/test-results", tags=["TestResults"])

@router.post("/", response_model=TestResultResponse, status_code=status.HTTP_201_CREATED)
def create_test_result(request: TestResultCreate, db: Session = Depends(get_db)):
    return crud.create_test_result(db, request)

@router.get("/", response_model=List[TestResultResponse])
def list_test_results(db: Session = Depends(get_db)):
    return crud.get_all_test_results(db)

@router.get("/{test_result_id}", response_model=TestResultResponse)
def get_test_result(test_result_id: int, db: Session = Depends(get_db)):
    db_result = crud.get_test_result(db, test_result_id)
    if not db_result:
        raise HTTPException(status_code=404, detail="TestResult not found")
    return db_result

@router.put("/{test_result_id}", response_model=TestResultResponse)
def update_test_result(test_result_id: int, request: TestResultUpdate, db: Session = Depends(get_db)):
    db_result = crud.update_test_result(db, test_result_id, request)
    if not db_result:
        raise HTTPException(status_code=404, detail="TestResult not found")
    return db_result

@router.delete("/{test_result_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_test_result(test_result_id: int, db: Session = Depends(get_db)):
    result = crud.delete_test_result(db, test_result_id)
    if not result:
        raise HTTPException(status_code=404, detail="TestResult not found")
    return {"ok": True}
