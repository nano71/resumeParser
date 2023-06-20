# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/19 17:27
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : tagGeneration.py
# @Software: IntelliJ IDEA

from datetime import datetime

from dateutil.relativedelta import relativedelta

start_date = datetime(1990, 1, 1)
end_date = datetime.now()
dates = []
result = []
current_date = start_date
while current_date <= end_date:
    # print(current_date.strftime('%Y.%m'))
    dates.append(current_date)
    current_date += relativedelta(months=1)

with open("../dict/time.text", "w", encoding="UTF-8") as file:
    for i, date in enumerate(dates):
        for date2 in dates[i + 1:]:
            file.write(date.strftime('%Y.%m') + "-" + date2.strftime('%Y.%m') + "/TIME" + "\n")
            print(date.strftime('%Y.%m') + "-" + date2.strftime('%Y.%m') + "/TIME")
        file.write(date.strftime('%Y.%m') + "-" + "至今" + "/TIME" + "\n")
        print(date.strftime('%Y.%m') + "-" + "至今" + "/TIME")
        file.write(date.strftime('%Y.%m') + "至今" + "/TIME" + "\n")
        print(date.strftime('%Y.%m') + "至今" + "/TIME")
