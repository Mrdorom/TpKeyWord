#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 14:16
# @Author : dorom
# @File : imindexPage.py
# @Software: PyCharm
from driverOption.baseApi import BaseApi
from utils.filePath import FilePath
from utils.readYaml import ReadYaml
import abc


class ClassGroupPage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,driver):
        self.driver = driver
        self.readyaml = ReadYaml()
        self.base = BaseApi(self.driver)
        self.imImdexPage = self.readyaml.getStream(FilePath.iOSImIndexPage)
        self.reconnect = self.imImdexPage.get("reconnect")
        self.search_button = self.imImdexPage.get("search_button")
        self.search_response = self.imImdexPage.get("search_response")
        self.adder_button = self.imImdexPage.get("adder_button")

        self.classGroupbutton = self.imImdexPage.get("classGroupbutton")
        self.class_search_button = self.imImdexPage.get("class_search_button")
        self.check_class_search_dest_button = self.imImdexPage.get("check_class_search_dest_button")
        self.key_body_search_button = self.imImdexPage.get("key_body_search_button")

    @abc.abstractmethod
    def imPageSearch(self):
        pass

    @abc.abstractmethod
    def switchAdders(self):
        """
        点击进入通讯录
        :return:
        """
        pass

class SwitchAdders(ClassGroupPage):
    """
    实现进入通讯录类
    """
    def imPageSearch(self):
        pass

    def switchAdders(self):
        self.base.iosClick(self.adder_button)
