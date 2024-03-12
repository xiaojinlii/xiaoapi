"""
官方文档——生命周期：https://fastapi.tiangolo.com/advanced/events/
"""

from fastapi import FastAPI
from application.settings import EVENTS
from contextlib import asynccontextmanager

from core.utils import import_modules_async


@asynccontextmanager
async def lifespan(app: FastAPI):
    await import_modules_async(EVENTS, "全局事件", app=app, status=True)

    yield

    await import_modules_async(EVENTS, "全局事件", app=app, status=False)
