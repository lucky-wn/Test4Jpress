# -*- coding: utf-8 -*-
# @Time : 2020/11/12 上午11:46
# @Author : ning
# @Email : 18301085980@163.com
# @File : main.py
# @Software: PyCharm
import time
import subprocess
import pytest
from utils.constant import report_folder

if __name__ == '__main__':
    pytest.main(['-s', '-a', '--alluredir', '%s' % report_folder])
