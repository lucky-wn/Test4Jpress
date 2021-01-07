# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午12:54 
# @Author : ning 
# @File : regist_page.py
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from engine.base_page import BasePage
from utils.constant import project
from utils.verify_code import VerifyCode


class RegistPage(BasePage):

    username_location = (By.NAME, 'username')
    email_location = (By.NAME, 'email')
    password_location = (By.NAME, 'pwd')
    confirm_pwd_location = (By.NAME, 'confirmPwd')
    captcha_location = (By.NAME, 'captcha')
    captcha_img_location = (By.ID, 'captchaimg')
    register_btn = (By.XPATH, "//*[@type='submit']")

    """注册页面"""
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def go_regist_page(self):
        self.driver.get("http://localhost:8080/jpress/user/register")
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_location)
        self.type_text(username, *self.username_location)

    def input_email(self, email):
        self.clear(*self.email_location)
        self.type_text(email, *self.email_location)

    def input_password(self, password):
        self.clear(*self.password_location)
        self.type_text(password, *self.password_location)

    def input_confirm_password(self, confirm_pwd):
        self.clear(*self.confirm_pwd_location)
        self.type_text(confirm_pwd, *self.confirm_pwd_location)

    def input_captcha(self, captcha):
        self.clear(*self.captcha_location)
        self.type_text(captcha, *self.captcha_location)

    def click_regist_btn(self):
        self.click(*self.register_btn)
        sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=project + os.sep + "chromedriver")
    rp = RegistPage(driver)
    rp.go_regist_page()
    rp.input_username("wang")
    rp.input_email("lll@126.com")
    rp.input_password("chen123")
    rp.input_confirm_password("chen123")
    captcha = VerifyCode.get_code(rp.driver, rp.captcha_img_location)
    rp.input_captcha(captcha)
    rp.click_regist_btn()
    rp.quit()