#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/2 17:58
# @Author : dorom
# @File : loginPage.py
# @Software: PyCharm


from utils.filePath import FilePath
from utils.readYaml import ReadYaml
from driverOption.baseApi import BaseApi
from errorExecption.eleNotFound import EleNotFound
from pageObjects.iOS.indexPage import IndexHolder


class Login(object):
    def __init__(self,driver):
        self.readYaml = ReadYaml()
        self.loginPage = self.readYaml.getStream(FilePath.iOSLaunchPage)
        self.base = BaseApi(driver)
        self.indexHolder = IndexHolder(driver)

        self.mobileLoginButton = self.readYaml.getNode(self.loginPage,"mobileLoginButton")
        self.account = self.readYaml.getNode(self.loginPage,"account")
        self.passwd = self.readYaml.getNode(self.loginPage,"passwd")
        self.submit = self.readYaml.getNode(self.loginPage,"submit")
        self.learnTitle = self.readYaml.getNode(self.loginPage,"learnTitle")
        self.skipButton = self.readYaml.getNode(self.loginPage,"skipButton")
        self.checkLoginButton = self.readYaml.getNode(self.loginPage,"checkLoginButton")

        self.settingButton = self.readYaml.getNode(self.readYaml.getStream(FilePath.iOSUserInfolPage),"settingButton")
        self.settingPage = self.readYaml.getStream(FilePath.iOSettinglPage)
        self.loginOutButton = self.readYaml.getNode(self.settingPage,"loginOutButton")
        self.affireButton = self.readYaml.getNode(self.settingPage,"affireButton")


    def login(self,account,password):
        self.loginout()
        mobileLoginEles = self.base.iosPredicates(self.mobileLoginButton)
        for loginButton in mobileLoginEles:
            visible = loginButton.get_attribute("visible")
            if visible == "true":
                loginButton.click()
                break

        if self.base.iosCheckElement(self.account):
            self.base.setValue(self.account,account,1)
            self.base.setValue(self.passwd,password,10)
            self.base.iosClick(self.submit)
        else:
            raise EleNotFound("输入账号框未找到")

    def checkLogin(self,checkCountFlage=5):
        """
        检查账号是否已经登录
        :param checkCountFlage:
        :return:
        """
        skipStast = self.skip()
        if skipStast:
            return skipStast
        flage = True
        checkCount = 0
        while flage and checkCount<checkCountFlage:
            if self.base.iosCheckElement(self.checkLoginButton):
                flage = False
                res = True
            if checkCount and checkCount==checkCountFlage-1:
                res = False
            checkCount+=1
        return res


    def loginout(self):
        if self.checkLogin(2):
            self.indexHolder.switchNavigation("我的")
            self.base.iosClick(self.settingButton)
            self.base.swipeDown()
            self.base.iosClick(self.loginOutButton)
            self.base.iosClick(self.affireButton)


    def skip(self):
        if self.base.iosCheckElement(self.skipButton,10):
            skipButton = self.base.iosPredicate(self.skipButton)
            flage = True
            findNum = 0
            while flage and findNum <4:
                status = skipButton.get_attribute("visible")
                if status:
                    self.base.iosClick(self.skipButton)
                    flage = False
                findNum +=1
                return True