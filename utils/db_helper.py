from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.todo import Base, Todo
import os

# Ensure the instance directory exists
os.makedirs('instance', exist_ok=True)

# SQLite database configuration
DATABASE_URL = "sqlite:///instance/todos.db"

environment_engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=environment_engine)

def init_db():
    Base.metadata.create_all(environment_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_todo(task):
    db = next(get_db())
    todo = Todo(task=task)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_todos():
    db = next(get_db())
    return db.query(Todo).order_by(Todo.created_at.desc()).all()