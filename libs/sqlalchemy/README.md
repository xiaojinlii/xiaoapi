# xiaoapi-sqlalchemy
[xiaoapi](https://github.com/xiaojinlii/xiaoapi)的sqlalchemy扩展包


## 安装
```
pip install xiaoapi-sqlalchemy
```


## 配置数据库连接url
在 application/settings 中 配置数据库连接url
```python
# 数据库配置项
# 连接引擎官方文档：https://docs.sqlalchemy.org/en/20/core/engines.html
# mysql配置说明：mysql+asyncmy://数据库用户名:数据库密码@数据库地址:数据库端口/数据库名称，需安装asyncmy
# sqlite配置说明：sqlite+aiosqlite:///数据库路径，需安装aiosqlite
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
```


## 创建表结构
在 application/settings 中 配置需要迁移的models
```python
# 数据库迁移
# 会将MIGRATE_MODELS里所有的model迁移到数据库表结构
MIGRATE_MODELS = [
    "modules.quickstart.models"
]
```

在命令行中使用以下命令创建表结构:
```
python manage.py sqlalchemy create-tables
```