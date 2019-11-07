# -*- coding:utf-8 -*-
'''
 # @Author: ChenYingzi
 # @Date: 2019-11-06 09:03:28
 # @LastEditors: ChenYingzi
 # @LastEditTime: 2019-11-07 14:02:54
 # @Description: 文件描述
'''

from app.libs.httper import HTTP
from flask import current_app

class YuShuBook:
    # 模型层 MVC结构的的M层

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        return result
        # url = self.isbn_url.format(isbn)

    @classmethod
    def search_by_keyword(cls, keyword, page):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        # dict
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']
