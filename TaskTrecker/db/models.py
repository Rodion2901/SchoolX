from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.database import Base

class TaskDB(Base):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    title = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())