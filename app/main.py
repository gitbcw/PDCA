import os
import importlib
import logging.config
from logging_config import logging_config

from fastapi import FastAPI

# 启用自定义日志配置
logging.config.dictConfig(logging_config)

app = FastAPI()

# 动态导入并包含所有路由
routers_path = os.path.join(os.path.dirname(__file__), 'routers')
for filename in os.listdir(routers_path):
    if filename.endswith('.py') and not filename.startswith('__'):
        module_name = f'app.routers.{filename[:-3]}'
        module = importlib.import_module(module_name)
        if hasattr(module, 'router'):
            app.include_router(module.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running!"}
