# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-07 09:28:48
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-07 10:52:26
 # Description: 文件描述
 # FilePath: \flaskdemo\fisher\app\forms\book.py
'''

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired
# 验证层
class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='关键字不能为空'),Length(min=1,max=30,message='ISBN或关键字无效')])
    page = IntegerField(validators=[NumberRange(min=1,max=99,message='请输入有效的页码1-99')],default=1)
    