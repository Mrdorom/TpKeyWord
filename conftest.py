#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/28 14:38
# @Author : dorom
# @File : conftest.py
# @Software: PyCharm

from driverOption.remoteDriver import RemoteDriver
from driverOption.setInputMethod import setSougo
from utils.logger import MyLogger
from utils.db import DbOption
import pytest


def pytest_addoption(parser):
    parser.addoption("--driverDict", action="store",
                     default="None",
                     help=" ’自定义 手机参数 用于启动Appium server '--driver' 添加到 pytest 配置中")


# 从配置对象获取 driverDict 的值
@pytest.fixture(scope='function')
def driverDict(pytestconfig):
    driverDict = pytestconfig.getoption('--driverDict')
    driverDict = eval(driverDict)
    return driverDict

@pytest.fixture()
def db():
    db = DbOption()
    return db

@pytest.fixture(scope="function")
def getUdid(driverDict):
    """
    返回设备的udid
    :param driverDict:
    :return:
    """
    udid = driverDict["udid"]
    return udid

@pytest.fixture(scope="function")
def driver(driverDict):
    """
    链接Appium server
    :param driverDict:
    :return:  driver
    """
    driver = RemoteDriver(driverDict).remoteDriver()
    return driver

@pytest.fixture(scope='function')
def driverFunc(driver,getUdid):
    """
    清理操作
    :param driver:
    :param getUdid:
    :return:
    """
    yield driverFunc
    setSougo(getUdid)
    driver.close_app()








