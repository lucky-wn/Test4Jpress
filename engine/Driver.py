# -*- coding: utf-8 -*-
# @Time : 2020/11/11 下午7:07
# @Author : ning
# @Email : 18301085980@163.com
# @File : Driver.py
# @Software: PyCharm
import os

from selenium import webdriver

from utils.constant import project


class Driver(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            chrome_driver = webdriver.Chrome(executable_path=project + os.sep + "chromedriver")
            orig = super(Driver, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
            cls._instance.driver = chrome_driver
        return cls._instance.driver