#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: ming yong
@file:test_json.py
@time:2021/05/26
"""
import requests

json_data = {'a': 1, 'b': 2}

r = requests.post("http://127.0.0.1:5000/add2", json=json_data)

print(r.headers)
print(r.text)