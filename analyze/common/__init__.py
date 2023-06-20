# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/6/16 23:32
# @Author : 梁皓 / nano71.com
# @Email : 1742968988@qq.com
# @File : __init__.py.py
# @Software: IntelliJ IDEA

import base64
import json
import math
import os
import re
from datetime import datetime, date

from LAC import LAC
from dateutil.relativedelta import relativedelta
from pypdf import PdfReader

from ocr_ecloud import CMSSEcloudOcrClient

accesskey = '613e43c93bf34345acd1786a49efbc6c'
secretkey = '1677beb41213436c9a8ca436f34dc194'
url = 'https://api-wuxi-1.cmecloud.cn:8443'
email_regex = r'[A-Za-z0-9._%+-]+,?@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'


class OCR:

    @staticmethod
    def file(imagepath, requesturl='/api/ocr/v1/webimage'):
        try:
            ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
            response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath=imagepath)
            return response.text

        except ValueError as e:
            print(e)

    @staticmethod
    def base64(imagepath="", requesturl='/api/ocr/v1/webimage'):
        with open(imagepath, 'rb') as f:
            img = f.read()
            image_base64 = base64.b64encode(img).decode('utf-8')
            ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
            response = ocr_client.request_ocr_service_base64(requestpath=requesturl, base64=image_base64)
            return response.text


class Extract:
    category: list[str] = ["校园经历", ""]
    need_label: list[str] = ["m", "PER", "LOC", "ORG", "TIME", "nz", "EB"]
    need_education: list[str] = ['小学', '初中', '高中', '中专', '大专', '本科', '硕士', '博士']
    school_characteristic_pattern = r"[\u4e00-\u9fa5]+(大学|学院|中学|小学|实验学校|高中|初中|小学|幼儿园)"
    base_info: dict = {}
    origin: str = ""
    text: str = ""
    lac_result: list[list[str]] = []
    lac_result_process: dict[str, list] = {}
    preselected: list[str] = []

    def __init__(self, text: str):
        self.origin = text
        self.text = text
        self.pretreatment()
        lac = LAC(model_path="../model/lac_model")
        lac.load_customization("../dict/interventionDictionary.text")
        self.lac_result = lac.run(self.text)
        self.remove_unnecessary()
        self.classify()

        # {
        #     "name": self.name(),
        #     "age": self.age(),
        #     "email": self.email(text),
        #     "highest_education": "",
        #     "school": "",
        #     "work_years": 0
        # }

    def initialize(self):
        print(self.origin)
        print(self.text)
        print(self.lac_result_process)
        print(self.lac_result)

        cache: dict = {
            "name": self.name(),
            "age": self.age(),
            "email": self.base_info["email"],
            "phone": self.phone(),
            "highest_education": self.highest_education(),
            "school": self.school(),
            "work_years": self.work_years()
        }
        self.base_info = cache

        return self.base_info

    def highest_education(self) -> str:
        if "EB" in self.lac_result_process:
            return max(self.lac_result_process["EB"], key=lambda x: self.need_education.index(x))
        return "无"

    def work_years(self):
        time_periods = self.lac_result_process["TIME"]

        for i, period in enumerate(time_periods):
            index: int = self.text.index(period)
            title_index_list = find_occurrences(self.text, r"工作经[历验]")
            end_index = find_occurrences(self.text, r"教育[(背景)(经历)]")

            print(period, index, title_index_list[0], end_index[0])
            print(self.text[title_index_list[0]:end_index[0]])

        print("time_periods: ", time_periods)
        time_periods = list(filter(lambda x: len(x) > 3, time_periods))

        def sort_by_prefix(string):
            return int(string[:4])

        time_periods = sorted(unique_list(time_periods), key=sort_by_prefix)
        print(time_periods)
        total_months = 0
        for i, period in enumerate(time_periods):

            if "-" not in period:
                break
            if re.search(r"\d{4}-\d{4}", period):
                start_year, end_year = period.split("-")
                period = f"{start_year}.01-{end_year}.01"
            if "至今" not in period and len(period) != 15:
                period = zero_fill(period)
            start_date_str, end_date_str = period.split('-')

            start_date = datetime.strptime(start_date_str.strip(), '%Y.%m')
            # 处理最后一个时间段
            if i == len(time_periods) - 1 and end_date_str == '至今':
                end_date = date.today()
            else:
                end_date = datetime.strptime(end_date_str.strip(), '%Y.%m')

            duration = relativedelta(end_date, start_date)
            total_months += duration.years * 12 + duration.months

        return math.ceil(total_months / 12)

    def remove_unnecessary(self):
        cache = [[], []]
        result = self.lac_result
        for i, item in enumerate(result[1]):
            if item in self.need_label or result[0][i] in self.need_education:
                cache[1].append(item)
                cache[0].append(result[0][i])
        self.lac_result = cache

    def classify(self):
        for i, label in enumerate(self.lac_result[1]):
            if label not in self.lac_result_process:
                self.lac_result_process[label]: list[str] = []
            self.lac_result_process[label].append(self.lac_result[0][i])

    def age(self) -> int:
        pattern = r"\d{2}\岁"
        matches = unique_list(re.findall(pattern, self.text))
        if matches:
            return matches[0].replace("岁", "")
        pattern = r"\b\d{4}\.\d{2}\b"
        matches = unique_list(re.findall(pattern, self.text))
        if not matches:
            lac_result_process = self.lac_result_process
            if "m" in lac_result_process:
                for item in unique_list(lac_result_process["m"]):
                    if contains_float_or_date(item):
                        matches.append(item)

            else:
                return 0
        pass
        current_date = datetime.now()
        for birthday in matches:
            if "." in birthday:
                parts = birthday.split(".")
                birth_date = datetime.strptime('.'.join(parts[:2]), '%Y.%m')
            else:
                birth_date = datetime.strptime(birthday, '%Y%m')

            age = current_date.year - birth_date.year

            if current_date.month < birth_date.month:
                age -= 1

            if age >= 18:
                self.text.replace(birthday, "")
                return age

    def phone(self) -> str:
        pattern = r"1[3-9]\d{1}\s?\d{4}\s?\d{4}"
        matches = unique_list(re.findall(pattern, self.text.replace(" ", "")))
        if matches:
            return matches[0]
        return "无"

    def email(self, text: str) -> str:
        """
        获取简历中的电子邮箱
        :param text: 要解析的简历文本
        :return: 电子邮箱
        """
        # self.base_info["email"] = self.email(text)
        emails = unique_list(re.findall(email_regex, text))
        self.text = comma_reduction(re.sub(email_regex, '', text))
        if emails:
            return emails[0].replace("@qa.com", "@qq.com").replace(",", "")
        return ""

    def name(self) -> str:
        """
        获取简历中的姓名
        :return: 姓名
        """
        person_names = self.lac_result_process["PER"]
        if person_names:
            return person_names[0]
        return ""

    def school(self) -> str:
        org: list = self.lac_result_process["ORG"]
        if org:
            for name in org:
                match = re.search(self.school_characteristic_pattern, name)
                if match:
                    return name
        return ""

    def pretreatment(self):
        text = self.text
        text = re.sub(r'([\w.]) +([.\w])', r"\1\2", text).replace(" ", "\n")
        text = re.sub(r'[\t\s]+', ",", text)
        text = re.sub(r"(\d{4})\.(\d\D)", r"\1.0\2", text)
        text = re.sub(r"(\d{4})-(\d{4})", r"\1.01-\2.01", text)
        text = re.sub(r"(\d{4})\.(\d)-?至今", r"\1.0\2-至今", text)
        text = re.sub(r"(\d{4})\.(\d{2})-?至今", r"\1.\2-至今", text)
        self.base_info["email"] = self.email(text)
        self.text = text
        pass


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


def unique_list(original_list: list) -> list:
    return list(set(original_list))


def comma_reduction(text: str) -> str:
    return re.sub(r',+', ',', text)


def read_doc(path: str) -> str:
    from docx2pdf import convert
    output_file = './cache-{}.pdf'.format(int(datetime.timestamp(datetime.now())))
    f1 = open(output_file, 'w')
    f1.close()
    convert(path, output_file)
    reader = PdfReader(output_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    os.remove(output_file)
    return text


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
