#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 14:16
# @Author : dorom
# @File : imindexPage.py
# @Software: PyCharm
from driverOption.baseApi import BaseApi
from utils.filePath import FilePath
from utils.readYaml import ReadYaml



class ClassGroup(object):
    def __init__(self,driver):
        self.driver = driver
        self.readyaml = ReadYaml()
        self.base = BaseApi(self.driver)
        self.imImdexPage = self.readyaml.getStream(FilePath.iOSImIndexPage)
        self.reconnect = self.imImdexPage.get("reconnect")
        self.search_button = self.imImdexPage.get("search_button")
        self.search_response = self.imImdexPage.get("search_response")
        self.adder_button = self.imImdexPage.get("adder_button")

    def imPageSearch(self):
        """
        点击进入通讯录
        :return:
        """
        self.base.iosClick(self.adder_button)

    def switchAdders(self):
        pass