# xiaoapi
基于FastAPI封装的快速开发框架


## 安装xiaoapi
```
pip install xiaoapi
```


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
```
python manage.py run-server
```


## demo演示
- https://github.com/xiaojinlii/xiaoapi-demo

## todo
依赖库版本号待优化