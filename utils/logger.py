#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/25 18:18
# @Author : dorom
# @File : logger.py
# @Software: PyCharm


import logging

from utils.filePath import FilePath
from utils.singLeton import singLeton
import time,os

@singLeton
class MyLogger(object):
    def __init__(self,funcName):
        self.log = logging.getLogger(funcName)
        self.log.setLevel(logging.INFO)
        self.logName = time.strftime("%Y-%m-%d",time.localtime(time.time())) +".log"
        self.fullLogName = os.path.join(FilePath.logPath,self.logName)

        # 创建 Filehandler
        fh = logging.FileHandler(self.fullLogName)
        fh.setLevel(logging.INFO)

        # 控制台输出  streamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        #设置输出格式
        formatter = logging.Formatter(
            "%(asctime)s -%(name)s- %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.log.addHandler(fh)
        self.log.addHandler(sh)

    def getlogger(self):
        return self.log

if __name__ == '__main__':
    logger = MyLogger("logger").getlogger()
    logger.info("ccc")
