# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/17 20:10
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : test3.py
# @Software: IntelliJ IDEA


import common

text = common.read_doc("../test_data/3.docx")
result = common.Extract(text).initialize()
print(result)


