#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 16:04
# @Author : dorom
# @File : imAdderPage.py
# @Software: PyCharm

import time
import abc
from driverOption.baseApi import BaseApi
from pageObjects.iOS.imIndexPage import ClassGroupPage
from pageObjects.iOS.loginPage import Login
from utils.filePath import FilePath
from utils.readYaml import ReadYaml


class ImAdderPage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,driver,db):

        self.readYaml = ReadYaml()
        self.base = BaseApi(driver)
        self.login = Login(driver)
        self.db = db
        self.classGroupPage = ClassGroupPage(driver)
        self.adderPage = self.readYaml.getStream(FilePath.iOSImAdderPage)
        self.add_friend_button = self.adderPage.get("add_friend_button")
        self.add_friend_textField = self.adderPage.get("add_friend_textField")
        self.keybody_search_button = self.adderPage.get("keybody_search_button")
        self.start_chat_button = self.adderPage.get("start_chat_button")
        self.addFriends = self.adderPage.get("addFriends")
        self.sendViryMsg = self.adderPage.get("sendViryMsg")
        self.cancelButton = self.adderPage.get("cancelButton")
        self.back_adder_button = self.adderPage.get("back_adder_button")
        self.back_im_list_button = self.adderPage.get("back_im_list_button")
        self.systemAddFriend = self.adderPage.get("systemAddFriend")
        self.agreeButton = self.adderPage.get("agreeButton")




    @abc.abstractmethod
    def addFirend(self,*args,**kwargs):
        """
        添加好友
        :return:
        """
        pass

    @abc.abstractmethod
    def newFridentSearch(self,*args,**kwargs):
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


class ApplyFriend(ImAdderPage):

    def addFirend(self,searchText):
        """
        添加好友
        :return:
        """

        # 2004000019
        self.classGroupPage.switchAdders()
        self.base.iosClick(self.add_friend_button)
        self.base.setValue(self.add_friend_textField, searchText, 1)
        time.sleep(2)
        self.base.iosClick(self.keybody_search_button)
        self.base.iosClick(self.addFriends)
        self.base.iosClick(self.sendViryMsg)  #第一次点击，收起键盘
        self.base.iosClick(self.sendViryMsg)  # 第二次点击，发送邀请

        self.base.iosClick(self.cancelButton)   # 取消 返回添加好友搜索页面
        self.base.iosClick(self.back_adder_button)  # 返回通讯录页面
        self.base.iosClick(self.back_im_list_button)  # 返回到班级首页
        self.login.login(searchText,'testtest')  # 登录申请添加好友的账号

    def agreeJoin(self):
        """
        同意添加好友
        :return:
        """
        self.classGroupPage.switchSystem()
        self.base.findElements(self.systemAddFriend)[0].click()
        self.base.findElements(self.agreeButton)[0].click()

    def newFridentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass

    def checkAddResult(self,userId,friendUserId):

        sql = "select `isFriend` from im_friend where userId={0} and `friendUserId`={1}".format(userId,friendUserId)
        querySet = self.db.select(sql)

        if querySet:
            if querySet[0][0] == 1:
                check1 = True
            else:
                return False
        else:
            return False
        sql2 = "select `isFriend` from im_friend where userId={0} and `friendUserId`={1}".format(userId,friendUserId)

        querySet2 = self.db.select(sql2)
        if querySet2:
            if querySet2[0][0] == 1:
                check2 = True
            else:
                return False
        else:
            return False

        if check1 and check2:
            return True

    def checkAddTearchAccount(self):
        """
        校验搜索的结果是老师
        :return:
        """
        if self.base.iosCheckElement(self.start_chat_button):
            try:
                self.base.iosClick(self.start_chat_button)
                #TODO: 聊天
            except:
                return False
        else:
            return False


class NewFrodentSearch(ImAdderPage):
    def addFirend(self, *args, **kwargs):
        pass

    def newFridentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass


class ImGroup(ImAdderPage):
    def addFirend(self, *args, **kwargs):
        pass

    def newFridentSearch(self, *args, **kwargs):
        pass

    def imGroup(self, groupName):
        pass