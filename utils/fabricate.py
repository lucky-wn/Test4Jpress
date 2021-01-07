# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午3:32 
# @Author : ning 
# @File : fabricate.py
import string
import random
import time


def random_string(length=None):
    """生成随机字符串，默认6位"""
    if not length:
        length = 6
    return "".join(random.sample(string.ascii_letters + string.digits, length))


if __name__ == '__main__':
    print(random_string(8))
    code = eval("random_string(8)")
    print(code)