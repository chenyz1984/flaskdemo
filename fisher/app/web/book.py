# -*- coding:utf-8 -*-
'''
 # @Author      : ChenYingzi
 # @Date        : 2019-11-06 09:03:28
 # @LastEditors : ChenYingzi
 # @LastEditTime: 2019-11-07 11:38:19
 # @Description : 文件描述
 # @FilePath    : /flaskdemo/fisher/app/web/book.py
'''

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify
from flask import request
from . import web
from app.forms.book import SearchForm

# http://127.0.0.1:5000/book/search/9787501524044/1
@web.route('/book/search')
def search():
    '''q page
        ?q=金庸&page=1
    '''
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    # return json.dumps(result), 200, {'content-type':'application/json'}
    else:
        return jsonify(form.errors)
