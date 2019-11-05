# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 15:00:51
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 15:02:13
 # Description: 文件描述
 # FilePath: \flaskdemo\fisher\fisher.py
'''
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<int:n>')
def hello(n):
    retstr = ''
    for i in range(n):
        retstr = retstr + '<li>' + str(i)+'-'+chr(i) + '</li>'
    return '<h1>Hello World</h1> '+retstr


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0',debug=True)