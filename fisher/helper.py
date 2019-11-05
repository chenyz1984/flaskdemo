# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 20:11:01
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 20:11:08
 # Description: 文件描述
 # FilePath: /flaskdemo/fisher/helper.py
'''

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():    
        isbn_or_key = 'isbn'
        
    short_word = word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    
    return isbn_or_key
