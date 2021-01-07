# -*- coding: utf-8 -*-
# @Time : 2020/11/11 下午5:15
# @Author : ning
# @Email : 18301085980@163.com
# @File : conftest.py
# @Software: PyCharm
import os
import time

import pytest
import allure

from engine.Driver import Driver
from utils.constant import report_folder


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    driver = Driver()
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver.switch_to.alert.accept()
        except:
            pass
        allure.attach(driver.get_screenshot_as_png(), '异常截图', allure.attachment_type.PNG)


def pytest_sessionfinish(session):
    """session结束时执行"""
    print("Finish！！！！！！！！！！！！！！！！！！！！！！！")
    Driver().quit()