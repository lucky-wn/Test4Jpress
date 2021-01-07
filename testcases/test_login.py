# -*- coding: utf-8 -*-
# @Time : 2020/11/11 下午4:31
# @Author : ning
# @Email : 18301085980@163.com
# @File : test_login.py
# @Software: PyCharm

import os
import time
from time import sleep

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from engine.Driver import Driver
from pages.login_page import LoginPage
from utils.log import get_logger
from utils.constant import project, screenshots_folder, report_folder
from utils import fabricate
from utils.ddt_reader import Reader
from utils.constant import ddt_folder
from utils.capture import capture


@allure.feature("用户登录页面")
class TestLogin(object):

    def setup(self):
        self.driver = Driver()
        print(id(self.driver))
        self.login_page = LoginPage(self.driver)
        self.login_page.go_login_page()

    @allure.title("检查登录功能")
    @pytest.mark.parametrize('username, password, expect', Reader.lines2list(ddt_folder + os.sep + 'login_ddt.txt'))
    def test_login(self, username, password, expect):
        with allure.step("输入账号"):
            self.login_page.input_username(username)
        with allure.step("输入密码"):
            self.login_page.input_password(password)
        with allure.step("点击登录按钮"):
            self.login_page.click_login_btn()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expect
        alert.accept()
        filename = self.login_page.get_shotcuts()
        allure.attach.file(filename, "登录截图", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])