#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/3 10:38
# @Author : dorom
# @File : personalPage.py
# @Software: PyCharm
from utils.filePath import FilePath
from utils.readYaml import ReadYaml
from driverOption.baseApi import BaseApi
from pageObjects.iOS.indexPage import IndexHolder
from errorExecption.eleNotFound import EleNotFound
from utils.db import DbOption
import abc,time


class PersonalHolder(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,driver):
        self.driver = driver
        self.db = DbOption()
        self.readYaml = ReadYaml()
        self.base = BaseApi(self.driver)
        self.indexHolder = IndexHolder(self.driver)
        self.userInfoPage = self.readYaml.getStream(FilePath.iOSUserInfolPage)

        # self.personalCenter = self.readYaml.getNode(self.userInfoPage,"personalCenter")
        self.personalButtons = self.readYaml.getNode(self.userInfoPage,"personalButtons")


        self.personalPage = self.readYaml.getStream(FilePath.iOSPersonalPage)

        self.saveButton = self.readYaml.getNode(self.personalPage,"saveButton")
        self.backButton = self.readYaml.getNode(self.personalPage,"backButton")


        self.updateNamePage = self.readYaml.getNode(self.personalPage,"updateNamePage")
        self.updateNameButton = self.readYaml.getNode(self.updateNamePage,"updateNameButton")
        self.updateNameInputButton = self.readYaml.getNode(self.updateNamePage,"updateNameInputButton")

        self.updateSummaryPage = self.readYaml.getNode(self.personalPage,"updateSummaryPage")
        self.updateSummaryButton = self.readYaml.getNode(self.updateSummaryPage,"updateSummaryButton")
        self.setSummary = self.readYaml.getNode(self.updateSummaryPage,"setSummary")
        self.ckectSummaryText = self.readYaml.getNode(self.updateSummaryPage,"ckectSummaryText")



    @abc.abstractmethod
    def update(self,*args,**kwargs):
        pass

    def clickPersonal(self):
        self.indexHolder.switchNavigation("我的")
        if self.base.iosCheckElements(self.personalButtons):
            buttons = self.base.iosPredicates(self.personalButtons)
            buttons[1].click()  #进入个人资料设置页面


class UpdateUserName(PersonalHolder):
    def update(self,newUserName):
        self.clickPersonal()
        if self.base.iosCheckElement(self.updateNameButton):
            self.base.iosClick(self.updateNameButton)
            self.base.setValue(newUserName,20)
            self.base.iosClick(self.saveButton)
            self.base.iosClick(self.backButton)
        else:
            raise EleNotFound("进入修改用户名页面失败")

    def checkUpdate(self,newUserName):
        """
        校验用户名修改成功
        :param newUserName:
        :return:
        """
        self.base.iosClick(self.updateNameButton)
        page = self.base.getPage()
        if newUserName in page:
            return True
        else:
            return False

class UpdateSummary(PersonalHolder):

    def update(self,summary):
        """
        修改个人简介
        :param summary:
        :return:
        """
        self.clickPersonal()
        if self.base.iosCheckElement(self.updateSummaryButton):
            self.base.iosClick(self.updateSummaryButton)
        else:
            raise EleNotFound("进入修改简介页面失败")
        self.base.setValue(summary,20)
        self.base.click(self.saveButton)
        self.base.click(self.backButton)

    def checkUpdateSummary(self,summary):
        """
        检查 
        :param summary:
        :return:
        """
        self.base.click(self.updateSummaryButton)
        page = self.base.getPage()
        if summary in page:
            return True
        else:
            return False