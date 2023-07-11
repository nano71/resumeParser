# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/17 20:10
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : test3.py
# @Software: IntelliJ IDEA


import common
import parser

text = common.read_doc("../test_data/7.docx")
# text = common.read_img("../test_data/test1.jpg")
# text = common.read_doc("../test_data/3.docx")
# text = common.read_doc("../test_data/4.docx")
# text = common.read_doc("../test_data/5.docx")
result = parser.Extract(text).initialize()
print(result)


