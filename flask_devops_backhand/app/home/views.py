#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 18:48
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: views.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from . import home
from flask_devops_backhand.app import User


#from app.home.forms import Userinfo

@home.route("/user_info")
def user_info():
    """查询数据
    user = str(User.query.count())
    return user
    """
    """添加数据"""
    # user01 = User(id=1, name='mikel_pan')
    # user02 = User(id=2, name='mikel_zhang')
    # db.session.add_all([user01, user02])
    # db.session.commit()
    user = str(User.query.count())
    user01 = User.query.all()
    print(user01)
    return user01



