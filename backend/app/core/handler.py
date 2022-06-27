from typing import Callable

from app.db.handler import connect_db, disconnect_db
from fastapi import FastAPI


def start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_db(app)

    return start_app


def stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await disconnect_db(app)

    return stop_app
