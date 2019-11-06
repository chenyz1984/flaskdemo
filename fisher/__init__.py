# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 23:15:25
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-06 20:08:10
 # Description: 文件描述
'''

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
