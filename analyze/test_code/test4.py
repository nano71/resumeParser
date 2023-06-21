# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/21 22:45
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : test4.py
# @Software: IntelliJ IDEA


import math
from datetime import datetime, date

from dateutil.relativedelta import relativedelta


def add_time_periods(*time_periods):
    total_months = 0

    for i, period in enumerate(time_periods):
        start_date_str, end_date_str = period.split('-')
        start_date = datetime.strptime(start_date_str.strip(), '%Y.%m')

        # 处理最后一个时间段
        if i == len(time_periods) - 1 and end_date_str.strip().lower() == '至今':
            end_date = date.today()
        else:
            end_date = datetime.strptime(end_date_str.strip(), '%Y.%m')

        duration = relativedelta(end_date, start_date)
        total_months += duration.years * 12 + duration.months

    return total_months


# 测试用例
time_periods = ['2020.2-2021.2', '2021.2-2022.3', '2022.3-至今']
total_months = add_time_periods(*time_periods)
print(math.ceil(total_months / 12))  # 这里的用例是 5年