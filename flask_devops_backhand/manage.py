#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 14:52
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: manage.py
# 开发团队：云飞国际
# 开发工具：PyCharm


from flask_devops_backhand.app import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import render_template

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    errors = 'errors'
    return render_template("home/404.html"), 404

if __name__ == '__main__':
    manager.run()