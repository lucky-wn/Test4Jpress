# -*- coding: utf-8 -*-
# @Time : 2020/11/4 下午5:50
# @Author : ning
# @Email : 18301085980@163.com
# @File : verify_code.py
# @Software: PyCharm
import os
import time

from PIL import Image

from utils.constant import temporary
from utils.chaojiying import Chaojiying_Client


class VerifyCode(object):

    @staticmethod
    def get_code(driver, location):
        """
        返回验证码识别的内容
        :param pic:
        :return:
        """

        pic_1 = temporary + os.sep + str(time.time()) + ".png"
        # 1.先截图
        driver.save_screenshot(pic_1)
        # 2.把验证码图抠出来
        ce = driver.find_element(*location)
        left = ce.location['x']
        top = ce.location['y']
        right = ce.size['width'] + left
        height = ce.size['height'] + top
        # 3.保存抠的图
        im = Image.open(pic_1)
        img = im.crop((left, top, right, height))
        pic_2 = temporary + os.sep + str(time.time()) + '.png'
        img.save(pic_2)
        cjy = Chaojiying_Client('18301085980', 'star000', '909506')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(pic_2, 'rb').read()
        return cjy.PostPic(im, 1902)['pic_str']


if __name__ == '__main__':
    print(VerifyCode.get_code("1604461029.9723651.png"))
