from typing import Annotated
from fastapi import APIRouter, Path

# создание марщрутов без подключения
# к основному проекту
# tags=["Items"] - свой раздел в документации
router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def list_items():
     return [
        "Item 1",
        "Item 2",
        "Item 3",
    ]

@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name" : "latest"}}

@router.get("/{item_id}/")
# item_id: int - должен быть только int
# Annotated[int, Path(ge=1)] - должно бьть число > 1 и менее 1 000 000
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        }
    }