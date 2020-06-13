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
        self.comePersonal = ClickPersonal(driver)
        self.indexHolder = IndexHolder(self.driver)
        self.userInfoPage = self.readYaml.getStream(FilePath.iOSUserInfolPage)

        self.personalPage = self.readYaml.getStream(FilePath.iOSPersonalPage)

        self.saveButton = self.readYaml.getNode(self.personalPage,"saveButton")
        self.backButton = self.readYaml.getNode(self.personalPage,"backButton")


        self.updateNamePage = self.personalPage.get("updateNamePage")
        self.updateNameButton = self.updateNamePage.get("updateNameButton")
        self.updateNameInputButton = self.updateNamePage.get("updateNameInputButton")

        self.updateSummaryPage = self.personalPage.get("updateSummaryPage")
        self.updateSummaryButton = self.updateSummaryPage.get("updateSummaryButton")
        self.setSummary = self.updateSummaryPage.get("setSummary")
        self.SummaryFlage = self.updateSummaryPage.get("SummaryFlage")

        self.updateSchoolButton = self.personalPage.get("updateSchoolButton")
        self.update_workButton = self.personalPage.get("update_workButton")



    @abc.abstractmethod
    def update(self,*args,**kwargs):
        pass



class UpdateUserName(PersonalHolder):
    def update(self,newUserName,db,mobile):
        self.comePersonal.clickPersonal(db,mobile)
        if self.base.iosCheckElement(self.updateNameButton):
            self.base.iosClick(self.updateNameButton)
            self.base.setValue(self.updateNameInputButton,newUserName,15)
            self.base.iosClick(self.saveButton)
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

    def update(self,summary,db,mobile):
        """
        修改个人简介
        :param summary:
        :return:
        """
        self.comePersonal.clickPersonal(db,mobile)
        if self.base.iosCheckElement(self.updateSummaryButton):
            self.base.iosClick(self.updateSummaryButton)
        else:
            raise EleNotFound("进入修改简介页面失败")
        self.base.iosClick(self.SummaryFlage)
        ele = self.base.iosPredicate(self.setSummary)
        ele.click()
        self.base.iosClearText(20)
        ele.set_value(summary)
        self.base.iosClick(self.saveButton)

    def checkUpdateSummary(self,summary):
        """
        检查 
        :param summary:
        :return:
        """
        self.base.iosClick(self.updateSummaryButton,30)
        page = self.base.getPage()
        if summary in page:
            return True
        else:
            return False


class UpdateSchool(PersonalHolder):

    def update(self,schoolName, db,mobile):
        self.comePersonal.clickPersonal(db, mobile)
        self.base.iosClick(self.updateSchoolButton)
        ele = self.base.iosPredicate(self.updateNameInputButton)
        ele.click()
        self.base.iosClearText(10)
        ele.set_value(schoolName)
        self.base.iosClick(self.saveButton)

    def checkUpdateSchool(self,schoolName):
        """
        检查
        :param schoolName:
        :return:
        """
        self.base.iosClick(self.updateSchoolButton,30)
        page = self.base.getPage()
        if schoolName in page:
            return True
        else:
            return False


class UpdateWorkspace(PersonalHolder):

    def update(self,workspaceName, db,mobile):
        self.comePersonal.clickPersonal(db, mobile)
        self.base.iosClick(self.update_workButton)
        ele = self.base.iosPredicate(self.updateNameInputButton)
        ele.click()
        self.base.iosClearText(10)
        ele.set_value(workspaceName)
        self.base.iosClick(self.saveButton)

    def checkUpdateWorkspace(self,workspaceName):
        """
        检查
        :param workspaceName:
        :return:
        """
        self.base.iosClick(self.update_workButton,30)
        page = self.base.getPage()
        if workspaceName in page:
            return True
        else:
            return False


class ClickPersonal(object):

    def __init__(self,driver):
        self.driver = driver
        self.base = BaseApi(driver)
        self.indexHolder = IndexHolder(driver)
        self.readYaml = ReadYaml()
        self.userInfoPage = self.readYaml.getStream(FilePath.iOSUserInfolPage)
        self.personalButtons = self.readYaml.getNode(self.userInfoPage,"personalButtons")


    def clickPersonal(self,db,mobile):
        """
        进入修改个人资料页面
        :param db:
        :param mobile:
        :return:
        """
        self.indexHolder.switchNavigation("我的")
        userName = db.select("select nickname from user where studentId= {0}".format(mobile))[0][0]
        self.personalButtons = self.personalButtons.format(userName)
        if self.base.iosCheckElements(self.personalButtons):
            button = self.base.iosPredicate(self.personalButtons)
            button.click()  #进入个人资料设置页面