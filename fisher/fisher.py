# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 15:00:51
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 15:02:13
 # Description: 文件描述
 # FilePath: \flaskdemo\fisher\fisher.py
'''
from flask import Flask,make_response
app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''q page'''
    #isbn isbn13 13个0-9纯数字
    #isbn10 10个0-9数字组成，含有‘-’
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():    
        isbn_or_key = 'isbn'
    short_q = q.replace('-','')
    if '-' in q and len(shot_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    pass


if __name__ == '__main__':
    app.debug = True
    
    app.run(host='0.0.0.0',debug=True)