from fastapi import APIRouter
from ..usecases.hello_usecase import HelloUseCase

router = APIRouter()

@router.get("/hello")
def hello(name: str = "World"):
    usecase = HelloUseCase()
    message = usecase.execute(name)
    return {"message": message}