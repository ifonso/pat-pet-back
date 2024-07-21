from fastapi import APIRouter, HTTPException
from src.controllers.controller import Controller
from src.types.requests import CreateProfissionalRequest


router = APIRouter()
controller = Controller()

@router.get("/profissionais", tags=["profissionais"])
async def get_profissionais():
    data = controller.get_profissionais()
    return data


@router.post("/profissionais", tags=["profissionais"])
async def create_profissional(request: CreateProfissionalRequest):
    try:
        data = controller.create_profissional(request)
        return data

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))