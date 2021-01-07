# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午12:40 
# @Author : ning 
# @File : base_page.py
import time
import os
#from PIL import ImageGrab

from utils.constant import screenshots_folder, report_folder


class BasePage(object):
    def __init__(self, driver):

        self.driver = driver

    def find_element(self, *loc):
        """获取元素"""
        return self.driver.find_element(*loc)

    def type_text(self, text, *loc):
        """输入内容"""
        self.find_element(*loc).send_keys(text)

    def clear(self, *loc):
        """清空"""
        self.find_element(*loc).clear()

    def click(self, *loc):
        """单击"""
        self.find_element(*loc).click()

    def get_title(self):
        """获取标题"""
        return self.driver.title

    def quit(self):
        self.driver.quit()

    def get_shotcuts(self):
        """selenium截图"""
        file_name = report_folder + os.sep + time.strftime("test_%Y%m%d%H%M%S") + ".png"
        self.driver.get_screenshot_as_file(file_name)
        return file_name

    # def get_pil_shotcuts(self):
    #     """PIL全屏截图"""
    #     im = ImageGrab.grab()
    #     file_name = report_folder + os.sep + time.strftime("test_%Y%m%d%H%M%S") + ".png"
    #     im.save(file_name)
    #     return file_name

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="../chromedriver")
    driver.get("http://www.baidu.com")
    bp = BasePage(driver)
    bp.get_shotcuts()