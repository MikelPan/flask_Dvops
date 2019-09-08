#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 14:52
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: config.py
# 开发团队：云飞国际
# 开发工具：PyCharm


import os

class Config:
    SECRET_KEY = 'plyx_yfgj'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def init_app(app):
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.174.134:3306/fkdevops?charset=utf8mb4'
    DEBUG = True

# the config for development
class MasterConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.174.134:3306/fkdevops?charset=utf8mb4'
    DEBUG = True

# define the config
config = {
    'default': MasterConfig,
    'dev': DevelopmentConfig
}
