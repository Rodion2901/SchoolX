from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routers.task import router as task_router
from db.init_db import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(task_router)