
from fastapi import APIRouter, Depends
from schemas import StudentBase, StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List



router = APIRouter(
    prefix='/student',
    tags=['student'],
)

# Router for creating a user
@router.post('/create', response_model=StudentCreate)
def create_user(request: StudentCreate, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Router for finding a user using id
@router.get('/find/{id}', response_model=StudentBase)
def get_user(id: str, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

@router.get('/getall', response_model=List[StudentBase])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)

@router.post('/update')
def update_user(id: str, request: StudentCreate, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)