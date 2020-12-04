from flask import Flask
from APP.extension import config_extension
from APP.config import envs

def create_app(config_name):
    # app 实例化
    app = Flask(__name__)
    # 导入所有的配置
    app.config.from_object(envs[config_name])
    envs[config_name].init_app(app)
    # 初始化第三方
    config_extension(app)
    # 配置相关蓝本



    return app
