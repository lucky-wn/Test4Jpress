# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午3:09 
# @Author : ning 
# @File : test_regist_page.py
import os
import time
from time import sleep

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from engine.Driver import Driver
from pages.regist_page import RegistPage
from utils.log import get_logger
from utils.constant import project, screenshots_folder, report_folder
from utils import fabricate
from utils.ddt_reader import Reader
from utils.constant import ddt_folder

logger = get_logger()


@allure.feature("用户注册页面")
class TestRegistPage(object):

    def setup(self):
        self.driver = Driver()
        print(id(self.driver))
        self.regist_page = RegistPage(self.driver)
        self.regist_page.go_regist_page()

    @allure.title("检查注册功能")
    @pytest.mark.parametrize('username, email, password, confirm_pwd, captcha, expect', Reader.lines2list(ddt_folder + os.sep + "regist_ddt.txt"))
    def test_regist(self, username, email, password, confirm_pwd, captcha, expect):
        with allure.step("输入用户名"):
            self.regist_page.input_username(username)
        with allure.step("输入邮箱"):
            self.regist_page.input_email(email)
        with allure.step("输入密码"):
            self.regist_page.input_password(password)
        with allure.step("输入确认密码"):
            self.regist_page.input_confirm_password(confirm_pwd)
        with allure.step("输入验证码"):
            self.regist_page.input_captcha(captcha)
        with allure.step("点击确认按钮"):
            self.regist_page.click_regist_btn()
        with allure.step("点击alert确定"):
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == expect
            alert.accept()
            file_name = self.regist_page.get_shotcuts()
            allure.attach.file(file_name, "用例截图", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', ''])