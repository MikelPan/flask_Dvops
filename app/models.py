#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 15:42
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: models.py
# 开发团队：云飞国际
# 开发工具：PyCharm


from . import db

from datetime import datetime

class User(db.Model):
    __tablename__ = "user_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    register_time = db.Column(db.DateTime, index=True, default=datetime.now)
    department = db.Column(db.String(100), unique=True)
    post = db.Column(db.String(100), unique=True)
    password = db.Column(db.VARCHAR(100), unique=True)
    email = db.Column(db.String(100), default=None)

    def __repr__(self):
        return "<User %r>" % self.name

