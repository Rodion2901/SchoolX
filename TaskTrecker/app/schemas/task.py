from pydantic import BaseModel
from datetime import datetime

class CreateTaskRequest(BaseModel):
    title:str
    status:str

class UpdateTaskRequest(BaseModel):
    title:str | None =None
    status:str | None=None

class TaskResponse(BaseModel):
    title:str
    status:str
    create_at:datetime
