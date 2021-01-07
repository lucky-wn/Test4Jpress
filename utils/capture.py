# -*- coding: utf-8 -*-
# @Time : 2020/11/11 下午6:51
# @Author : ning
# @Email : 18301085980@163.com
# @File : capture.py
# @Software: PyCharm
import allure


def capture(function):
    def wrapper(*args, **kw):
        print(args, kw)
        try:
            function(*args, **kw)
        except Exception as e:
            print(e.args)
    return wrapper