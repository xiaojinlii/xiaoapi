# xiaoapi-elasticsearch
xiaoapi-elasticsearch


需要在 application/settings 中 添加以下配置：
```python
# Elasticsearch 配置
ELASTICSEARCH_ENABLE = False
ELASTICSEARCH_USER = "elastic"
ELASTICSEARCH_PASSWORD = "gv3Z0Nnti2gdApgzLmUN"
ELASTICSEARCH_URL = "http://127.0.0.1:9200"
```

然后在 application/settings 中的 EVENTS 里引入 
```python
EVENTS = [
    "xiaoapi_elasticsearch.connect_elasticsearch",
]
```