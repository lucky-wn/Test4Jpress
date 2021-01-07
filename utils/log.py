# -*- coding: utf-8 -*-
# @Time : 2020/11/7 上午10:29
# @Author : ning
# @File : log.py

import logging
import logging.handlers
import datetime
import os

from utils.constant import log


def get_logger():
    logger = logging.getLogger('myLogger')
    logger.setLevel(logging.DEBUG)
    # 根据时间滚动,when=midnight表示凌晨12点开始记录日志,interval表示间隔,backupCount表示备份数量
    rf_handler = logging.handlers.TimedRotatingFileHandler(log + os.sep + 'all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(log + os.sep + 'error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.debug("test debug")
    logger.error("test error")