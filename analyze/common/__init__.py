# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/16 23:32
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : __init__.py.py
# @Software: IntelliJ IDEA
import json
import os
import re
from datetime import datetime

import pdfplumber


def unique_list(original_list: list) -> list:
    return list(dict.fromkeys(original_list))


def comma_reduction(text: str) -> str:
    return re.sub(r',+', ',', text)


def contains_float_or_date(text: str) -> bool:
    cache = text.replace(r"[,.]", "")
    length = len(cache)
    if length < 5 or length > 8 or cache[0] != "1":
        return False
    return True


def zero_fill(date_range: str) -> str:
    # 解析日期范围
    start_date, end_date = date_range.split("-")
    # 将字符串转换为日期对象
    start_date = datetime.strptime(start_date, "%Y.%m")
    end_date = datetime.strptime(end_date, "%Y.%m")

    # 判断月份是否需要补零
    start_month = str(start_date.month).zfill(2)
    end_month = str(end_date.month).zfill(2)

    # 构建新的日期范围字符串
    return f"{start_date.year}.{start_month}-{end_date.year}.{end_month}"


def find_occurrences(text: str, pattern) -> list[int]:
    occurrences = [match.start() for match in re.finditer(pattern, text)]
    return occurrences


def get_jobs() -> list[str]:
    jobs = []
    with open('../dict/jobs.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去除文本中的换行符
            if len(line):
                jobs.append(line)
    return jobs


def new_line():
    print("\n")
    print("--------------------")
    print("\n")


def split_by_list(text: str, mark_list: list[str], skip_item: bool = False) -> list[str]:
    split_list: list[str] = []
    start_index = 0
    for i, item in enumerate(mark_list):
        index: int = text.find(item, start_index)
        if index != -1:
            split_list.append(text[start_index:index])
            start_index = index if skip_item else index + len(item)
    split_list.append(text[start_index:])
    return split_list


def str_exist(text: str, re_exp: str) -> bool:
    res = re.search(re_exp, text)
    if res:
        return True
    return False


def cn_exist(text) -> bool:
    res = re.search(r"[\u4e00-\u9fa5]", text)
    if res:
        return True
    return False


def is_left_right_layout(arr):
    length = len(arr)
    count = 0
    # 遍历数组，计算大于100的数的数量
    for num in arr:
        if num > 100:
            count += 1
    # 判断大于100的数的数量是否超过数组长度的一半
    if count > length / 2:
        return True
    return False


# 求最大差中值
def find_max_difference_median(nums):
    max_diff = float('-inf')  # 初始化差值为负无穷大
    max_diff_pair = None  # 初始化差值最大的相邻元素对

    # 遍历数组，计算最大差值和相邻元素对
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])  # 计算相邻元素之间的差值
        if diff > max_diff:
            max_diff = diff
            max_diff_pair = (nums[i], nums[i + 1])

    # 计算中位数
    median = (max_diff_pair[0] + max_diff_pair[1]) / 2

    return median


def dict2json(file_name, the_dict):
    """
    将字典文件写如到json文件中
    :param file_name: 要写入的json文件名(需要有.json后缀),str类型
    :param the_dict: 要写入的数据，dict类型
    :return: True代表写入成功,False代表写入失败
    """
    try:
        json_str = json.dumps(the_dict, indent=4)
        with open(file_name, 'w') as json_file:
            json_file.write(json_str)
        return True
    except ValueError:
        return False


def read_doc(path: str) -> str:
    from docx2pdf import convert
    output_file = './cache-{}.pdf'.format(int(datetime.timestamp(datetime.now())))
    f1 = open(output_file, 'w')
    f1.close()
    convert(path, output_file)
    # reader = PdfReader(output_file)
    text = ""
    weight_list = []
    box_list = []
    with pdfplumber.open(output_file) as pdf:
        # 遍历每个页面
        for page in pdf.pages:
            # 提取页面文本和文本位置信息
            for obj in page.extract_words():
                text += obj["text"] + "\n"
                x0, top, x1, bottom = obj["x0"], obj["top"], obj["x1"], obj["bottom"]
                width = x1 - x0
                height = bottom - top

                # print("Text: ", obj["text"])
                # print("Position: x0=", x0)
                if width > 10:
                    box_list.append([x0, top, obj["text"]])
                    weight_list.append(x0)
                # print("Size: width=", width, "height=", height)
    # for page in reader.pages:
    #     text += page.extract_text()
    if is_left_right_layout(weight_list):
        print("左右布局")
        mid = find_max_difference_median(sorted(weight_list))
        print("中值:", mid)
        # box_list =  sorted(same_row_merge(box_list), key=layout_sort)
        box_list = same_row_merge(box_list)

        first_list = list(filter(lambda x: x[0] < mid, box_list))
        second_list = list(filter(lambda x: x[0] > mid, box_list))
        merged_array = [x[2] for x in first_list + second_list]
        cache = ""
        for item in merged_array:
            cache += item + "\n"
        text = cache
        new_line()
        print(first_list, second_list)
        new_line()

    os.remove(output_file)
    return text


def layout_sort(data):
    return data[0], data[1]


def same_row_merge(data_list):
    merged_data = {}
    result = []

    for item in data_list:
        key = item[1]  # 获取索引1的值作为键
        if key not in merged_data:
            merged_data[key] = item  # 将数据项添加到字典中
            result.append(item)  # 添加到结果列表中
        else:
            merged_data[key][2] += ' ' + item[2]  # 将文本值合并到已存在的数据项中
    return result
