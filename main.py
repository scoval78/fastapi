from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    # Load the ML model
    await create_tables()
    print("База готова к работе")
    yield
    # Clean up the ML models and release the resources
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
