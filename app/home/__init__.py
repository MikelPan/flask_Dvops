#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 14:51
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: __init__.py.py
# 开发团队：云飞国际
# 开发工具：PyCharm



from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views