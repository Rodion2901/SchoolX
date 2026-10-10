from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.task import CreateTaskRequest, UpdateTaskRequest
from app.repositories.task import TaskRepository


class TaskServices:
    def get_list(db:Session):
        tasks = TaskRepository.get_list(db)
        return tasks
    def get_task(task_id:int, db:Session):
        task = TaskRepository.get_task(task_id, db)
        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        return task
    def create_task(data: CreateTaskRequest, db:Session):
        title = data.title.strip()
        if not title:
            raise HTTPException(
                status_code=422,
                detail="Task title can't be empty"
            )
        try:
            task = TaskRepository.create_task(db, title=title, status=data.status)
            db.commit()
        except Exception:
            db.rollback()
            raise
        db.refresh(task)
        return task
    def update_task(task_id:int, data:UpdateTaskRequest, db:Session):
        if data.title or data.status is None:
            raise HTTPException(
                status_code=422,
                detail="One of inputs is Null"
            )
        try:
            task = TaskRepository.update_task(task_id, data, db)
            if task is None:
                raise HTTPException(
                    status_code=404,
                    detail="Task not found"
                )
            db.commit()
        except Exception:
            db.rollback()
        db.refresh(task)
        return task
    def delete_task(task_id:int, db:Session):
        try:
            task = TaskRepository.get_task(task_id, db)
            if task is None:
                raise HTTPException(
                    status_code=404,
                    detail="Task not found"
                )
            result = TaskRepository.delete_task(task_id, db)
            db.commit()
        except Exception:
            db.rollback
        db.refresh(task)
