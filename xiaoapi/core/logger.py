"""
# 日志简单配置
# 具体其他配置 可自行参考 https://github.com/Delgan/loguru
"""

import os
from loguru import logger
from ..conf import settings


# 移除控制台输出
# logger.remove(handler_id=None)

if hasattr(settings, 'BASE_DIR'):
    log_path = os.path.join(settings.BASE_DIR, 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    log_path_info = os.path.join(log_path, 'info.log')
    log_path_error = os.path.join(log_path, 'error.log')

    info = logger.add(log_path_info, rotation="00:00", retention="30 days", enqueue=True, encoding="UTF-8", level="INFO")
    error = logger.add(log_path_error, rotation="00:00", retention="30 days", enqueue=True, encoding="UTF-8", level="ERROR")
