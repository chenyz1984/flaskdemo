# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 23:12:26
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-06 20:06:30
 # Description: 文件描述
'''

from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book