#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/25 16:56
# @Author : dorom
# @File : filePath.py
# @Software: PyCharm


import os

class FilePath(object):
    """
    项目配置文件路径
    """
    basePath = os.path.join(os.path.abspath(os.path.dirname(__file__)).split('TpKeyWord')[0],"TpKeyWord")
    logPath = os.path.join(basePath,"log")  # 日志目录
    dbConfigPath = os.path.join(basePath,"config/dbConfig.yaml")  #数据库配置文件
    appiumLog = os.path.join(basePath,"appiumLog") # appium Log
    reportPath = os.path.join(basePath,"report")  # 测试结果目录

    androidDriverPath = os.path.join(basePath,"config/AndroidDriver.yaml")   #Android 设备配置文件
    androidTestDir = os.path.join(basePath, "test/Android") # android 测试用例检索目录
    iOSTestDir = os.path.join(basePath, "test/iOS") # android 测试用例检索目录

    # Android Params
    androidLoginParams = os.path.join(basePath, "data/Android/loginParams.yaml")

    # iOS Params
    iOSLoginParams = os.path.join(basePath, "data/iOS/iOSLoginParams.yaml")


    # Android page
    androidPagePath = os.path.join(basePath,"pageObjectConfig/Android")  # Android pages Element Base path
    androidLaunchPage = os.path.join(androidPagePath,"launch.yaml")
    androidIndexPage = os.path.join(androidPagePath,"index.yaml")
    androidUserInfoPage = os.path.join(androidPagePath,'myself/userInfoPage.yaml')
    androidPersonalPage = os.path.join(androidPagePath,'myself/personal.yaml')
    androidSettingPage = os.path.join(androidPagePath,"myself/settingPage.yaml")
    androidGroup = os.path.join(androidPagePath,"classAndGrade/group.yaml")

    # iOS Page
    iOSPagePath = os.path.join(basePath,"pageObjectConfig/iOS")
    iOSLaunchPage = os.path.join(iOSPagePath,"launch.yaml")
    iOSIndexPage = os.path.join(iOSPagePath,"index.yaml")
    iOSUserInfolPage = os.path.join(iOSPagePath,"myself/userInfoPage.yaml")
    iOSettinglPage = os.path.join(iOSPagePath,"myself/settingPage.yaml")
    iOSPersonalPage = os.path.join(iOSPagePath,"myself/personalPage.yaml")
    iOSImIndexPage = os.path.join(iOSPagePath,"im/imindex.yaml")
    iOSImAdderPage = os.path.join(iOSPagePath,"im/adder.yaml")
    iOSImChatPage = os.path.join(iOSPagePath,"im/imChat.yaml")


if __name__ == '__main__':
    f = FilePath()

    #