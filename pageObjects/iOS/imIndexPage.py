#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 14:16
# @Author : dorom
# @File : imindexPage.py
# @Software: PyCharm

from driverOption.baseApi import BaseApi
from utils.filePath import FilePath
from utils.readYaml import ReadYaml


class ClassGroupPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.readyaml = ReadYaml()
        self.base = BaseApi(self.driver)
        self.imImdexPage = self.readyaml.getStream(FilePath.iOSImIndexPage)
        self.reconnect = self.imImdexPage.get("reconnect")
        self.searchButton = self.imImdexPage.get("searchButton")
        self.searchFild = self.imImdexPage.get("searchFild")
        self.QuestionResonse = self.imImdexPage.get("QuestionResonse")
        self.DoubtResonse = self.imImdexPage.get("DoubtResonse")
        self.classGroupResonse = self.imImdexPage.get("classGroupResonse")

        self.addressButton = self.imImdexPage.get("addressButton")
        self.systemNotice = self.imImdexPage.get("systemNotice")
        self.doubtButton = self.imImdexPage.get("doubtButton")
        self.classGroupButton = self.imImdexPage.get("classGroupButton")


    def switchSystem(self):
        """
        点击进入系统消息
        :return:
        """
        self.base.iosClick(self.systemNotice)

    def switchAdders(self):
        """
        点击进入通讯录
        :return:
        """
        self.base.iosClick(self.addressButton)

    def indexSearch(self,searchContent,searchType):
        """
        校园首页搜索
        :param searchContent:
        :param searchType:
        :return:
        """
        pass

    def switchDoubt(self):
        """
        选择问答
        :return:
        """
        self.base.iosClick(self.doubtButton)

    def switchClassGroup(self):
        """
        选择班级
        :return:
        """
        self.base.iosClick(self.classGroupButton)