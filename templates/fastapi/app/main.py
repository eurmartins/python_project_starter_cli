from fastapi import FastAPI
from app.api.v1.example import router as example_router

app = FastAPI()

app.include_router(example_router, prefix="/api/v1")
