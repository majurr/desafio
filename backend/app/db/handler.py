import logging

from app.core.config import DATABASE_URL
from databases import Database
from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def connect_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database
    except Exception as _err:
        logger.warn("***** ERROR OPEN PGSQL *****")
        logger.warn(_err)
        logger.warn("***** ERROR OPEN PGSQL *****")


async def disconnect_db(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as _err:
        logger.warn("***** ERROR CLOSE PGSQL *****")
        logger.warn(_err)
        logger.warn("***** ERROR CLOSE PGSQL *****")
