from sqlalchemy.orm import Session
from schemas import StudentBase, StudentCreate, StudentUpdate
from db.models import User
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: StudentCreate):
    new_user = User(
        firstname = request.firstname,
        middlename = request.middlename,
        lastname = request.lastname,
        course = request.course,
        email = request.email,
        password = Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, id: str):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user
    
def get_all_user(db: Session):
    return db.query(User).all()

def update_user(db: Session, id: str, request: User):
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    
    user.update({
        User.firstname: request.firstname,
        User.middlename: request.middlename,
        User.lastname: request.lastname,
        User.course: request.course,
        User.email: request.email,
        User.password: Hash.bcrypt(request.password),
    })
    db.commit()
    return {
        'message' : f'User with id {id} has been updated'
    }
