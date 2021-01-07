# -*- coding: utf-8 -*-
# @Time : 2020/11/11 下午5:07
# @Author : ning
# @Email : 18301085980@163.com
# @File : admin_login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from engine.base_page import BasePage


class AdminLoginPage(BasePage):
    """管理员登录页面"""
    username_location = (By.NAME, "user")
    password_location = (By.NAME, "pwd")
    captcha_location = (By.NAME, "captcha")
    login_btn_location = (By.XPATH, "//*[@type='submit']")

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def go_admin_login_page(self):
        self.driver.get("http://localhost:8080/jpress/admin/login")
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_location)
        self.type_text(username, *self.username_location)

    def input_password(self, password):
        self.clear(*self.password_location)
        self.type_text(password, *self.password_location)

    def input_captcha(self, captcha):
        self.clear(*self.captcha_location)
        self.type_text(captcha, *self.captcha_location)

    def click_login_btn(self):
        self.click(*self.login_btn_location)