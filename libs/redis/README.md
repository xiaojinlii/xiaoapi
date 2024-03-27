# xiaoapi_redis
xiaoapi_redis


需要在 application/settings 中 添加以下配置：
```python
# Redis 数据库配置
# 格式："redis://:密码@地址:端口/数据库名称"
REDIS_DB_ENABLE = False
REDIS_DB_URL = "redis://:123456@177.8.0.5:6379/1"
```

然后在 application/settings 中的 EVENTS 里引入 
```python
EVENTS = [
    "xiaoapi_redis.connect_redis",
]
```