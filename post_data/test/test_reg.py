#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: ming yong
@file:test_reg.py
@time:2021/05/26
"""

import requests

user_info = {'name': 'zhangsan', 'password': 'lisi'}
r = requests.post("http://127.0.0.1:5000/register", data=user_info)

print(r.text)