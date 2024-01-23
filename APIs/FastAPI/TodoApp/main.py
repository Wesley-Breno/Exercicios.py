from fastapi import FastAPI
from routers import todos, auth, admin
from src.database import engine
from src import models

app = FastAPI()
app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)

models.Base.metadata.create_all(bind=engine)
