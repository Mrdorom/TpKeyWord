#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/26 18:21
# @Author : dorom
# @File : appiumServer.py
# @Software: PyCharm
import os
import subprocess
import time

import requests,re
from utils.filePath import FilePath
from driverOption.closeWebdriver import CloseWebdriver
from utils.logger import MyLogger


class AppiumServer(object):

    def __init__(self,host,port,udid,webDriver=None):
        self.logger = MyLogger("AppiumServer").getlogger()
        self.host = host
        self.port = port
        self.udid = udid
        self.webDriver = webDriver

    def startAppiumServer(self):
        """
        启动Appium Server
        :param host: 启动的本地ip
        :param port: 启动端口
        :param udid: 绑定的udid
        """
        bootStarpPort = str(self.port+1)
        cmd = " appium -a {0} -p {1} -bp {2} -U {3}".format(self.host, self.port, bootStarpPort,self.udid)
        appium_log = os.path.join(FilePath.appiumLog, str(self.port) + '.log')
        if os.path.exists(appium_log):
            os.remove(appium_log)
        if self.checkPort():
            self.logger.info("端口：{0}已被占用".format(self.port))
            self.stopPort()
        subprocess.Popen(cmd, shell=True, stdout=open(appium_log, 'a'), stderr=subprocess.STDOUT)
        flage = False
        checkCount = 0
        while not flage and checkCount<7:
            time.sleep(1)
            flage = self.checkPort()
            if flage:
                self.logger.info("端口：{0} Appium 系统服务启动成功".format(self.port))
            if not flage and checkCount==6:
                self.logger.info("端口：{0} Appium 系统服务启动成功".format(self.port))
            checkCount +=1

    def checkPort(self):
        """
        端口检查
        :return: check res
        """
        try:
            requests.get("http://{0}:{1}/wd/hub/status".format(self.host, self.port))
            res = True
        except:
            res = False
        return res

    def stopPort(self):
        """
        关闭appium server
        :param port:
        :return:
        """
        if self.webDriver:   # 关闭webDriver
            CloseWebdriver().closeWebdriver(self.webDriver)

        cmd = "ps -ef | grep {0}".format(self.port) + "| awk '{print $2}'"
        pid_list = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        pattrn = re.compile(r"(\d+)")
        for pid in pid_list:
            cmd = 'kill -9 {0}'.format(pattrn.findall(str(pid))[0])
            os.system(cmd)
        self.logger.info("端口:{0}退出成功".format(self.port))