# fastapi
基于FastAPI的封装

requires-python = ">=3.8"

## 安装xiaoapi
`pip install git+https://github.com/xiaojinlii/xiaoapi.git`

## 创建项目
创建项目目录及项目文件
`python -m xiaoapi.admin create-project --name project_name`

如果项目路径已存在，并且在项目路径下，可直接使用以下命令创建项目文件
`python -m xiaoapi.admin create-project-files`

创建项目后，会新增一下目录结构：
```
.
├── application
│   ├── __init__.py
│   ├── routes.py       # 主路由配置文件
│   ├── settings.py     # 项目配置文件
└── manage.py           # 命令管理器，使用"python manage.py --help"查看全部命令
```

## 启动服务
`python manage.py run-server`

## 创建表结构
创建表结构需要在 application/settings 的 MIGRATE_MODELS 中配置模型

`python manage.py create-tables`

## 创建模块
`python manage.py create-module --name module_name`

## demo演示
- https://github.com/xiaojinlii/fastapi-demo