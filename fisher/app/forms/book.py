# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-06 21:12:58
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-06 21:13:34
 # Description: 文件描述
'''
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='关键字不能为空'),Length(min=1,max=30,message='ISBN或关键字无效')])
    page = IntegerField(validators=[NumberRange(min=1,max=99,message='请输入有效的页码1-99')],default=1)
    