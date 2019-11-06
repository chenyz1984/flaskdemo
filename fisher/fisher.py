# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 19:59:20
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-06 20:01:30
 # Description: 文件描述
'''


from flask import Flask
from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
