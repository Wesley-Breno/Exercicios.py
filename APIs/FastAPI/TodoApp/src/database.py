from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URI_DATABSE = 'sqlite:///./todosapp.db'

engine = create_engine(
    URI_DATABSE,
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
