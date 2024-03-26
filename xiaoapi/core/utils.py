import importlib
from .logger import logger


def import_modules(modules: list, desc: str):
    """动态导入模块"""
    for module in modules:
        if not module:
            continue
        # try:
        importlib.import_module(module)
        # except ModuleNotFoundError:
        #     logger.error(f"AttributeError：导入{desc}失败，未找到该模块：{module}")


def import_functions(modules: list, desc: str, **kwargs):
    """动态导入模块，并且执行函数"""
    for module in modules:
        if not module:
            continue
        # try:
        module_name = module[0:module.rindex(".")]
        module_function = module[module.rindex(".") + 1:]
        module_pag = importlib.import_module(module_name)
        getattr(module_pag, module_function)(**kwargs)
        # except ModuleNotFoundError:
        #     logger.error(f"ModuleNotFoundError：导入{desc}失败，未找到该模块：{module}")
        # except AttributeError:
        #     logger.error(f"AttributeError：导入{desc}失败，未找到 {module} 模块下的方法：{function}")


async def import_functions_async(modules: list, desc: str, **kwargs):
    """动态导入模块，并且执行函数"""
    for module in modules:
        if not module:
            continue
        # try:
        module_name = module[0:module.rindex(".")]
        module_function = module[module.rindex(".") + 1:]
        module_pag = importlib.import_module(module_name)
        await getattr(module_pag, module_function)(**kwargs)
        # except ModuleNotFoundError:
        #     logger.error(f"ModuleNotFoundError：导入{desc}失败，未找到该模块：{module}")
        # except AttributeError:
        #     logger.error(f"AttributeError：导入{desc}失败，未找到 {module} 模块下的方法：{function}")
