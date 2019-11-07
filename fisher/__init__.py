# -*- coding:utf-8 -*-
'''
 # @Author: ChenYingzi
 # @Date: 2019-11-06 09:03:28
 # @LastEditors: ChenYingzi
 # @LastEditTime: 2019-11-07 15:18:24
 # @Description: 文件描述
'''

from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
