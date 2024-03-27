# xiaoapi-mongodb
xiaoapi-mongodb

需要在 application/settings 中 添加以下配置：
```python
# MongoDB 数据库配置
# 格式：mongodb://用户名:密码@地址:端口/?authSource=数据库名称
MONGO_DB_ENABLE = False
MONGO_DB_NAME = "fastapi"
MONGO_DB_URL = f"mongodb://admin:123456@177.8.0.6:27017/?authSource={MONGO_DB_NAME}"
```

然后在 application/settings 中的 EVENTS 里引入 
```python
EVENTS = [
    "xiaoapi_mongodb.connect_mongo",
]
```