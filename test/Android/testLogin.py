#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 11:08
# @Author : dorom
# @File : testLogin.py
# @Software: PyCharm

import pytest
from pageObjects.Android.loginPage import LoginPage
from utils.filePath import FilePath
from utils.readYaml import ReadYaml

accountData = ReadYaml().getStream(FilePath.androidLoginParams)

loginParams = []
for account in accountData:
    params = []
    params.append(account["account"])
    params.append(account["password"])
    loginParams.append(params)


@pytest.mark.parametrize("userName, password", loginParams)
class TestLogin(object):

    def testLogin(self,userName,password,driver,driverFunc):
        login = LoginPage(driver)
        login.login(userName,password)
        assert login.checkLogin()