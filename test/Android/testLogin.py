#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 11:08
# @Author : dorom
# @File : testLogin.py
# @Software: PyCharm

import pytest
from driverOption.remoteDriver import RemoteDriver
from pageObjects.Android.loginPage import LoginPage
from utils.logger import MyLogger

data = [(13755321731,"testtest")]


@pytest.mark.parametrize("userName, password", data)
class TestLogin(object):

    def testLogin(self,userName,password,driver,driverFunc):
        logger = MyLogger(self.__class__.__name__).getlogger()
        login = LoginPage(driver)
        login.login(userName,password)
        assert login.checkLogin()