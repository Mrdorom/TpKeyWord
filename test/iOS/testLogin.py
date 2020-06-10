#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/2 20:19
# @Author : dorom
# @File : login.py
# @Software: PyCharm


import pytest
from pageObjects.iOS.loginPage import Login
from utils.filePath import FilePath
from utils.readYaml import ReadYaml

accountData = ReadYaml().getStream(FilePath.iOSLoginParams)

loginParams = []
for account in accountData:
    params = []
    params.append(account["account"])
    params.append(account["password"])
    loginParams.append(params)


@pytest.mark.parametrize("userName, password", loginParams)
class TestLogin(object):

    def testLogin(self,userName,password,driver,iosTearDown):
        login = Login(driver)
        login.login(userName,password)
        assert login.checkLogin(2)