#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 09:31
# @Author : dorom
# @File : loginPage.py
# @Software: PyCharm
import time

from utils.filePath import FilePath # 配置文件路径
from utils.logger import MyLogger # 日志
from utils.readYaml import ReadYaml
from driverOption.baseApi import BaseApi
from errorExecption.eleNotFound import EleNotFound


class LoginPage(object):
    """
    登录类
    """
    def __init__(self,driver):
        self.driver = driver
        self.logger = MyLogger(self.__class__.__name__).getlogger()
        self.baseView = BaseApi(self.driver)
        self.launchPath = FilePath().androidLaunchPage
        self.readYaml =  ReadYaml()
        self.readYaml.getStream(self.launchPath)   # 获取yaml数据流
        self.launchEle = self.readYaml.stream.get("launch",False)  # 读取到本页数据
        self.checkLoginEle = self.readYaml.stream.get("ckeckLogin",False)  # 登录成功校验元素

    def login(self,userName,password):
        """
        登录
        :param userName: 账号
        :param password: 密码
        :return:
        """
        self.mobileLoginButton = self.readYaml.getNode(self.launchEle,"mobileLoginButton")
        self.aaccount = self.readYaml.getNode(self.launchEle,"aaccount")
        self.passwd = self.readYaml.getNode(self.launchEle,"passwd")
        self.submitButton = self.readYaml.getNode(self.launchEle,"submitButton")
        self.forgetPasswd = self.readYaml.getNode(self.launchEle,"forgetPasswd")

        if self.baseView.checkElement(self.mobileLoginButton):
            self.baseView.click(self.mobileLoginButton)
        else:
            raise EleNotFound("账号登录按钮未找到")
        if self.baseView.checkElement(self.aaccount):
            self.baseView.sendKeys(self.aaccount,userName)
            self.baseView.sendKeys(self.passwd,password)
            self.baseView.click(self.submitButton)
        else:
            raise EleNotFound("输入账号按钮未找到")

    def checkLogin(self):
        """
        多次容错检查 首页探索元素
        :return: bool
        """
        checkFlage = True
        checkCount = 0
        while checkFlage and checkCount<5:
            if self.baseView.checkElement(self.readYaml.getNode(self.checkLoginEle,"explore"),10):
                checkFlage = False
                res = True
            if checkCount and checkCount==4:
                res = False
            checkCount+=1
        return res

if __name__ == '__main__':
    l = LoginPage(1)
