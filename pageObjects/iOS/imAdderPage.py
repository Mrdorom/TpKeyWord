#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 16:04
# @Author : dorom
# @File : imAdderPage.py
# @Software: PyCharm
import time
import abc
from driverOption.baseApi import BaseApi
from pageObjects.iOS.imindexPage import SwitchAdders
from utils.filePath import FilePath
from utils.readYaml import ReadYaml


class ImAdderPage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,driver):

        self.readYaml = ReadYaml()
        self.base = BaseApi(driver)
        self.switchAddersClass = SwitchAdders(driver)
        self.adderPage = self.readYaml.getStream(FilePath.iOSImAdderPage)
        self.add_friend_button = self.adderPage.get("add_friend_button")
        self.add_friend_textField = self.adderPage.get("add_friend_textField")
        self.keybody_search_button = self.adderPage.get("keybody_search_button")
        self.start_chat_button = self.adderPage.get("start_chat_button")
        self.cancel_button = self.adderPage.get("cancel_button")
        self.back_adder_button = self.adderPage.get("back_adder_button")
        self.back_im_list_button = self.adderPage.get("back_im_list_button")

    @abc.abstractmethod
    def addFirend(self,*args,**kwargs):
        """
        添加好友
        :return:
        """
        pass

    @abc.abstractmethod
    def newFrodentSearch(self,*args,**kwargs):
        """
        新朋友搜索
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abc.abstractmethod
    def imGroup(self,groupName):
        """
        班组
        :param groupName: 班组名称
        :return:
        """
        pass


class AdderFriend(ImAdderPage):

    def addFirend(self,searchText):
        """
        添加好友
        :return:
        """
        self.base.iosClick(self.add_friend_button)
        self.base.setValue(self.add_friend_textField, searchText, 1)
        time.sleep(2)
        self.base.iosClick(self.keybody_search_button)

    def newFrodentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass

    def checkAddStudentAccount(self):
        """
        校验搜索的结束是学员
        :return:
        """

    def checkAddTearchAccount(self):
        """
        校验搜索的结果是老师
        :return:
        """


class NewFrodentSearch(ImAdderPage):
    def addFirend(self, *args, **kwargs):
        pass

    def newFrodentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass


class ImGroup(ImAdderPage):
    def addFirend(self, *args, **kwargs):
        pass

    def newFrodentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass