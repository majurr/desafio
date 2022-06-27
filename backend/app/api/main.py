from app.api.routes import router as api_router
from app.core import config, handler
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def get_api():
    app = FastAPI(title="Desafio 1", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", handler.start_app_handler(app))
    app.add_event_handler("shutdown", handler.stop_app_handler(app))

    app.include_router(api_router, prefix="/api")

    return app


app = get_api()
