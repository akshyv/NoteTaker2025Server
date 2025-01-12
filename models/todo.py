from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }