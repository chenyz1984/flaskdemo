# -*- coding:utf-8 -*-
'''
 # Author: ChenYingzi
 # Date: 2019-11-05 20:15:55
 # LastEditors: ChenYingzi
 # LastEditTime: 2019-11-05 22:32:02
 # Description: 文件描述
'''

import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):

        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
