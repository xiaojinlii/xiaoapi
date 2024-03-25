"""
官方文档——生命周期：https://fastapi.tiangolo.com/advanced/events/
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from .utils import import_functions_async
from ..conf import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await import_functions_async(settings.EVENTS, "全局事件", app=app, status=True)

    yield

    await import_functions_async(settings.EVENTS, "全局事件", app=app, status=False)
