# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 23:15:25
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 23:28:13
 # Description: 文件描述
'''
from flask import Flask


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app
