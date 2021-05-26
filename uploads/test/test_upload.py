#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: ming yong
@file:test_upload.py
@time:2021/05/26
"""

import requests

file = r'D:\tmp\0969.jpg'
file_data = {'image': open(file, 'rb')}

user_info = {'info': 'Lenna'}

r = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)

print(r.text)