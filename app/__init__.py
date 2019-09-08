#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 14:50
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: __init__.py.py
# 开发团队：云飞国际
# 开发工具：PyCharm



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 注册蓝图
    from app.home import home as home_blueprint
    from app.admin import admin as admin_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app