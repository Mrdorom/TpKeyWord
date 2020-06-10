#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/9 17:26
# @Author : dorom
# @File : testPersonal.py
# @Software: PyCharm

from pageObjects.iOS.personalPage import UpdateUserName,UpdateSummary,UpdateSchool,UpdateWorkspace
import time

mobile = 13788881212


class  TestUpdateUserName(object):

    def testUpdateUserName(self,driver,iosTearDown,db):
        """
        测试修改用户名
        :param driver:
        :param iosTearDown:
        :return:
        """
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        userName = "iosUpdate" + tm
        userName = userName[:14]
        update = UpdateUserName(driver)
        update.update(userName,db,mobile)
        assert update.checkUpdate(userName)


class TestUpdateSummary(object):

    def testUpdateSummary(self,driver,iosTearDown,db):
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        userSummary = "iosSummary" + tm
        userSummary = userSummary[:14]
        update = UpdateSummary(driver)
        update.update(userSummary,db,mobile)
        assert update.checkUpdateSummary(userSummary)

class TestUpdateSchool(object):

    def testUpdateSchool(self,driver,iosTearDown,db):
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        SchoolName = "清华" + tm
        SchoolName = SchoolName[:14]
        update = UpdateSchool(driver)
        update.update(SchoolName,db,mobile)
        assert update.checkUpdateSchool(SchoolName)


class TestUpdateWorkspace(object):

    def testUpdateWorksapce(self,driver,iosTearDown,db):
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        WorkName = "BT学院" + tm
        WorkName = WorkName[:14]
        update = UpdateWorkspace(driver)
        update.update(WorkName,db,mobile)
        assert update.checkUpdateWorkspace(WorkName)