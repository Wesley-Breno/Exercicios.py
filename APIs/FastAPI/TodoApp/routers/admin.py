from fastapi import APIRouter, Depends, HTTPException
from src.database import SessionLocal
from src.models import Todos
from routers.auth import get_current_user
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/todos', status_code=200)
async def get_all_todos(
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)],
):
    if user.get('role') != 'admin' or user is None:
        raise HTTPException(401, 'Authentication failed. You not is a Admin.')

    return db.query(Todos).all()


@router.delete('/todo/{id_todo}', status_code=204)
async def delete_a_todo(
        id_todo: int,
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)],
):
    if user.get('role') != 'admin' or user is None:
        raise HTTPException(401, 'Authentication failed. You not is a Admin.')

    todo = db.query(Todos).filter(Todos.id == id_todo).first()
    if todo is None:
        raise HTTPException(404, 'Data not found.')

    db.delete(todo)
    db.commit()
