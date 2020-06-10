#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/26 16:53
# @Author : dorom
# @File : remoteDriver.py
# @Software: PyCharm

from errorExecption.dataTypeError import DataTypeError
from errorExecption.driverTypeError import DriverTypeError
from appium import webdriver
from utils.logger import MyLogger


class RemoteDriver(object):
    def __init__(self,capabilitiesData):
        self.logger = MyLogger(self.__class__.__name__).getlogger()
        if not isinstance(capabilitiesData,dict):
            raise DataTypeError("启动数据类型错误")
        self.capabilitiesData = capabilitiesData
        platformName = capabilitiesData["platformName"]

        self.Capabilities = {}
        self.Capabilities["platformName"] = platformName
        self.Capabilities["platformVersion"] = capabilitiesData["platformVersion"]
        self.Capabilities["deviceName"] = capabilitiesData["deviceName"]
        self.Capabilities["deviceName"] = capabilitiesData["deviceName"]
        if platformName.upper() =="ANDROID":
            self.Capabilities["appPackage"] = capabilitiesData["appPackage"]
            self.Capabilities["appActivity"] = capabilitiesData["appActivity"]
            # Chrome webDriver Path
            self.Capabilities["chromedriverExecutable"] = capabilitiesData["chromedriverExecutable"]
            self.Capabilities["automationName"] = "uiAutomator2"
            self.Capabilities["autoGrantPermissions"] = True # 自动获取需要哪些权限
            self.Capabilities["unicodeKeyboard"] = True # 使用Appium 自带的输入法
            self.Capabilities["resetKeyboard"] = True  # 输入法复位
            self.Capabilities["uiautomator2ServerLaunchTimeout"] = 72000  # Appium 新命令间隔时间
        elif platformName.upper() == "IOS":
            self.Capabilities["automationName"] = "XCUITest"
            self.Capabilities["bundleId"] = capabilitiesData["bundleId"]
            self.Capabilities["xcodeSigningId"] = "iPhone Developer"
            self.Capabilities["xcodeOrgId"] = capabilitiesData["xcodeOrgId"]
            self.Capabilities["wdaLocalPort"] = capabilitiesData["wdaLocalPort"]    # iOS  wda代理端口设置（用于控制多机测试）
            self.Capabilities["webkitResponseTimeout"] = 1000
            self.Capabilities["useNewWDA"] = True     #暂时还不清楚有什么用
            self.Capabilities["autoAcceptAlerts"] = True     #自动处理警告
            self.Capabilities["startIWDP"] = True
            self.Capabilities["usePrebuiltWDA"] = True  # 不再重新安装WDA
        else:
            raise DriverTypeError("{0} 的手机类型不存在，只支持Android、iOS".format(platformName))

        self.Capabilities["udid"] = capabilitiesData["udid"]
        self.Capabilities["noReset"] = True
        self.Capabilities["recreateChromeDriverSessions"] = True # 如果driver 切换到原生的context 下就关闭webdriver
        self.Capabilities["systemPort"] = capabilitiesData["systemPort"]
        self.Capabilities["newCommandTimeout"] = 72000

    def remoteDriver(self):
        """
        手机连接Appium server
        :return: Driver
        """
        remoteUrl = "http://{0}:{1}/wd/hub".format(str(self.capabilitiesData["host"]),str(self.capabilitiesData["port"]))
        driver = webdriver.Remote(remoteUrl,self.Capabilities)
        return driver