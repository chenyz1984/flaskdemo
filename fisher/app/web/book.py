# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 21:34:21
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 22:26:06
 # Description: 文件描述
'''
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import jsonify,Blueprint

#蓝图blueprint


web = Blueprint('web',__name__)
# http://127.0.0.1:5000/book/search/9787501524044/1
@web.route('/book/search/<q>/<page>')
def search(q, page):
    '''q page'''
    # isbn isbn13 13个0-9纯数字
    # isbn10 10个0-9数字组成，含有‘-’
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type':'application/json'}
