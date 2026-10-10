from sqlalchemy.orm import Session
from sqlalchemy import select

from app.schemas.task import CreateTaskRequest, UpdateTaskRequest, TaskResponse
from db.models import TaskDB

class TaskRepository:
    def get_list(db:Session):
        statement = select(TaskDB)
        tasks = db.scalars(statement).all()
        return tasks
    def get_task(task_id:int, db:Session):
        task = db.get(TaskDB, task_id)
        return task
    def create_task(db:Session, title:str, status:str):
        task = TaskDB(
            title = title,
            status = status
        )
        db.add(task)
        return task
    def update_task(task_id:int,data:UpdateTaskRequest, db:Session):
        task = db.get(TaskDB, task_id)
        if task is None:
            return task
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)
        return task
    def delete_task(task_id:int, db:Session):
        task = db.get(TaskDB, task_id)
        if task is None:
            return task
        db.delete(task)