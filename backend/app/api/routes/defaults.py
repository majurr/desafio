import imp
from typing import List

from fastapi import APIRouter

# roteador padrão
router = APIRouter()


@router.get("/")
async def get_all() -> List[dict]:
    defaults = [
        {"id": 1, "'name": "Mario"},
        {"id": 2, "'name": "Luzia"},
        {"id": 3, "'name": "Leni"},
        {"id": 4, "'name": "Lara"},
        {"id": 5, "'name": "Gustavo"},
    ]

    return defaults
