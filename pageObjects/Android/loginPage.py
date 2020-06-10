#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 09:31
# @Author : dorom
# @File : loginPage.py
# @Software: PyCharm

from utils.filePath import FilePath # 配置文件路径
from utils.logger import MyLogger # 日志
from utils.readYaml import ReadYaml # 获取元素
from driverOption.baseApi import BaseApi # 元素操作
from errorExecption.eleNotFound import EleNotFound
from pageObjects.Android.indexPage import MySelf


class LoginPage(object):
    """
    登录类
    """
    def __init__(self,driver):
        self.driver = driver
        self.logger = MyLogger(self.__class__.__name__).getlogger() # 获取日志
        self.baseView = BaseApi(self.driver)
        self.launchPath = FilePath().androidLaunchPage
        self.readYaml =  ReadYaml()
        self.myself = MySelf(driver)


        self.launchPage = self.readYaml.getStream(self.launchPath)
        self.launchEle = self.launchPage.get("launch",False)
        self.checkLoginEle = self.launchPage.get("ckeckLogin",False)  # 登录成功校验元素

        self.mobileLoginButton = self.readYaml.getNode(self.launchEle, "mobileLoginButton")
        self.aaccount = self.readYaml.getNode(self.launchEle, "aaccount")
        self.passwd = self.readYaml.getNode(self.launchEle, "passwd")
        self.submitButton = self.readYaml.getNode(self.launchEle, "submitButton")
        self.forgetPasswd = self.readYaml.getNode(self.launchEle, "forgetPasswd")

        self.androidUserInfoPage = self.readYaml.getStream(FilePath.androidUserInfoPage)
        self.settingPage = self.readYaml.getStream(FilePath.androidSettingPage)

        self.settingButton = self.readYaml.getNode(self.androidUserInfoPage,"settingButton")
        self.loginOutButton = self.readYaml.getNode(self.settingPage,"loginOutButton")
        self.affirmLoginoutButton = self.readYaml.getNode(self.settingPage,"affirmLoginoutButton")

    def login(self,userName,password):
        """
        登录
        :param userName: 账号
        :param password: 密码
        :return:
        """
        self.loginOut()  # 如果已登录会退出登录

        if self.baseView.checkElement(self.mobileLoginButton):
            self.baseView.click(self.mobileLoginButton)
        else:
            raise EleNotFound("账号登录按钮未找到")
        if self.baseView.checkElement(self.aaccount):
            self.baseView.sendKeys(self.aaccount,userName)
            self.baseView.sendKeys(self.passwd,password)
            self.baseView.click(self.submitButton)
            print('登录成功')
        else:
            raise EleNotFound("输入账号按钮未找到")

    def checkLogin(self,checkCountFlage=5):
        """
        多次容错检查 首页探索元素
        :return: bool
        """
        checkFlage = True
        checkCount = 0
        while checkFlage and checkCount<checkCountFlage:
            if self.baseView.checkElement(self.readYaml.getNode(self.checkLoginEle,"explore"),5):
                checkFlage = False
                res = True
            if checkCount and checkCount==checkCountFlage-1:
                res = False
            checkCount+=1
        return res

    def loginOut(self):
        if self.checkLogin(3):   #检查是否已经登录
            self.myself.chooseNavigation()
            if self.baseView.checkElement(self.settingButton):
                self.baseView.click(self.settingButton)
                self.baseView.click(self.loginOutButton)
                self.baseView.click(self.affirmLoginoutButton)

if __name__ == '__main__':
    l = LoginPage(1)

