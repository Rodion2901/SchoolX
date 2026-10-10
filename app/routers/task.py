from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session

from db.database import get_db
from app.schemas.task import CreateTaskRequest, TaskResponse, UpdateTaskRequest
from app.service.task import TaskServices
router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("",response_model=list[TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    result = TaskServices.get_list(db)
    return result

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id:int, db:Session = Depends(get_db)):
    result = TaskServices.get_task(task_id, db)
    return result

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(data:CreateTaskRequest, db: Session = Depends(get_db)):
    result = TaskServices.create_task(data,db)
    return result
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id:int, data:UpdateTaskRequest, db: Session = Depends(get_db)):
    result = TaskServices.update_task(task_id,data,db)
    return result

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id:int, db: Session = Depends(get_db)):
    result = TaskServices.delete_task(task_id, db)