# -*- coding: utf-8 -*- 
# @Time : 2020/11/7 下午3:43 
# @Author : ning 
# @File : ddt_reader.py
import os
import re

from utils.constant import ddt_folder, utils_folder
from utils import fabricate


class Reader(object):
    @staticmethod
    def lines2list(filepath):
        sample = []
        with open(filepath) as f:
            lines = f.readlines()
        for line in lines:
            # 使用井号做为注释
            if line.startswith("#"):
                continue
            if line.endswith("\n"):
                line = line.replace("\n", "")

            special_word = re.findall(r'(\$\{[0-9a-zA-Z_]*\(.*\)\})', line)
            if special_word:
                for word in special_word:
                    line = line.replace(word, eval("fabricate.%s" % word[2:-1]))
            # 去掉长度为0的字符串
            line2be_add = line.split("<%>")
            if '' in line2be_add:
                line2be_add.remove('')
            sample.append(tuple(line2be_add))
        return sample


if __name__ == '__main__':
    import sys
    sys.path.append(utils_folder)
    sys.path.insert(0, utils_folder)
    print(sys.path)
    for line in Reader.lines2list(ddt_folder + os.sep + "regist_ddt.txt"):
        print(line)