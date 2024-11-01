from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database.database import Base
from datetime import datetime, UTC

class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    tasks = relationship("Task", back_populates="input")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    input_id = Column(Integer, ForeignKey('inputs.id'))
    task_content = Column(Text, nullable=False)
    suggestions = Column(Text)
    status = Column(String(50), default='未完成')
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC))
    input = relationship("Input", back_populates="tasks")
