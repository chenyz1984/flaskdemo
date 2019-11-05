# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 19:59:20
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 22:02:19
 # Description: 文件描述
'''


from flask import Flask

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
