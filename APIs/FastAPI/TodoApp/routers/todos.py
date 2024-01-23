from fastapi import APIRouter, Depends, HTTPException
from src.database import SessionLocal
from src.models import Todos
from routers.auth import get_current_user
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter(
    prefix='/todos',
    tags=['todos']
)


class TodoForm(BaseModel):
    title: str
    description: str
    priority: int
    complete: bool = False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def get_all_todos(
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)]
):
    if user is None:
        raise HTTPException(401, 'Authentication failed ;(')
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()


@router.post('/create', status_code=201)
async def create_a_todo(
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)],
        form_todo: TodoForm

):
    if user is None:
        raise HTTPException(401, 'Authentication failed ;(')
    todo = Todos(**form_todo.model_dump(), owner_id=user.get('id'))
    db.add(todo)
    db.commit()


@router.put('/update/{id_todo}', status_code=204)
async def update_a_todo(
        id_todo: int,
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)],
        form_todo: TodoForm
):
    if user is None:
        raise HTTPException(401, 'Authentication failed ;(')

    todo = db.query(Todos).filter(Todos.id == id_todo).filter(Todos.owner_id == user.get('id')).first()
    if todo is None:
        raise HTTPException(404, 'Data not found.')

    todo.title = form_todo.title
    todo.description = form_todo.description
    todo.priority = form_todo.priority
    todo.complete = form_todo.complete
    db.add(todo)
    db.commit()


@router.delete('/delete/{id_todo}', status_code=204)
async def delete_a_todo(
        id_todo: int,
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)],
):
    if user is None:
        raise HTTPException(401, 'Authentication failed ;(')

    todo = db.query(Todos).filter(Todos.id == id_todo).filter(Todos.owner_id == user.get('id')).first()
    if todo is None:
        raise HTTPException(404, 'Data not found.')

    db.delete(todo)
    db.commit()
    