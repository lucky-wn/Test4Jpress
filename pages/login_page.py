# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午12:47 
# @Author : ning 
# @File : login_page.py
from selenium.webdriver.common.by import By

from engine.base_page import BasePage


class LoginPage(BasePage):
    """用户登录页面"""
    username_location = (By.NAME, "user")
    password_location = (By.NAME, "pwd")
    login_btn_location = (By.XPATH, "//*[@type='submit']")

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def go_login_page(self):
        self.driver.get("http://localhost:8080/jpress/user/login/")
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_location)
        self.type_text(username, *self.username_location)

    def input_password(self, password):
        self.clear(*self.password_location)
        self.type_text(password, *self.password_location)

    def click_login_btn(self):
        self.click(*self.login_btn_location)