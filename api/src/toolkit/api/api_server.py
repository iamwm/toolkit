# Created by wangmeng at 2020/11/19
from fastapi import FastAPI

from toolkit.api.handlers.host_handler import router as host_router


def create_app():
    app = FastAPI()
    app.include_router(host_router, prefix='/api')
    return app
