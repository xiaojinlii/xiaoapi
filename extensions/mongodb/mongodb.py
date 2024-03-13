"""
mongodb连接
博客：https://www.cnblogs.com/aduner/p/13532504.html
mongodb 官网：https://www.mongodb.com/docs/drivers/motor/
motor 文档：https://motor.readthedocs.io/en/stable/

需要安装：
pip install aioredis==2.0.1
pip install redis==5.0.1
"""

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from application.settings import MONGO_DB_URL, MONGO_DB_NAME


async def connect_mongo(app: FastAPI, status: bool):
    """
    把 mongo 挂载到 app 对象上面
    :param app:
    :param status:
    :return:
    """
    if status:
        client: AsyncIOMotorClient = AsyncIOMotorClient(
            MONGO_DB_URL,
            maxPoolSize=10,
            minPoolSize=10,
            serverSelectionTimeoutMS=5000
        )
        app.state.mongo_client = client
        app.state.mongo = client[MONGO_DB_NAME]
        # 尝试连接并捕获可能的超时异常
        try:
            # 触发一次服务器通信来确认连接
            data = await client.server_info()
            print("MongoDB 连接成功", data)
        except Exception as e:
            raise ValueError(f"MongoDB 连接失败: {e}")
    else:
        print("MongoDB 连接关闭")
        app.state.mongo_client.close()
