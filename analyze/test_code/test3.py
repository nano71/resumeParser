# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/16 23:56
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : test3.py
# @Software: IntelliJ IDEA
import json
import tkinter as tk

from PIL import Image

import common


def size(imagepath):
    image = Image.open(imagepath)
    return image.size


def test():
    imagepath = "../test.jpeg"
    result = json.loads(common.OCR.file(imagepath=imagepath))
    imagesize = size(imagepath)
    window = tk.Tk()
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # 创建画布并关联滚动条
    canvas = tk.Canvas(window, yscrollcommand=scrollbar.set, width=imagesize[0], height=800)

    def on_mouse_scroll(event):
        # 根据滚轮的方向，向上滚动为 -1，向下滚动为 1
        direction = -1 if event.delta > 0 else 1
        canvas.yview_scroll(direction, 'units')

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # 配置滚动条和画布的关联
    scrollbar.config(command=canvas.yview)

    # 创建内部框架并在画布上放置
    frame = tk.Frame(canvas)
    canvas.create_window(0, 0, anchor=tk.NW, window=frame)
    i = 0

    common.dict2json("../cache/ocr_result.json", result)
    rows = []
    positions = []
    if "body" in result:
        rows = list(map(lambda x: x["word"], result["body"]["content"]["prism_wordsInfo"]))
        positions = list(map(lambda x: x["position"], result["body"]["content"]["prism_wordsInfo"]))
    elif "items" in result:
        rows = list(map(lambda x: x["itemstring"], result["items"]))
    print(rows)
    print(common.Extract((','.join(rows), ','.join(rows))).initialize())
    common.dict2json("../cache/ocr_positions.json", positions)
    for position in positions:
        points = [(point["x"], point["y"]) for point in position]
        canvas.create_polygon(points, outline='black', fill='')
        i += 1

    # 绑定鼠标滚轮事件
    canvas.bind('<MouseWheel>', on_mouse_scroll)
    canvas.config(scrollregion=canvas.bbox(tk.ALL))
    window.mainloop()


test()
