from fastapi import FastAPI
from .interfaces.hello_controller import router as hello_router

app = FastAPI()

app.include_router(hello_router, prefix="/api/v1")