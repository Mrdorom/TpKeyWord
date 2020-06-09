#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/9 17:26
# @Author : dorom
# @File : testPersonal.py
# @Software: PyCharm

from pageObjects.iOS.personalPage import UpdateUserName,UpdateSummary
import time


class  TestUpdateUserName(object):

    def testUpdateUserName(self,driver,iosTearDown):
        """
        测试修改用户名
        :param driver:
        :param iosTearDown:
        :return:
        """
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        userName = "ios Update" + tm
        update = UpdateUserName(driver)
        update.update(userName)
        assert update.checkUpdate(userName)


class TestUpdateSummary(object):

    def testUpdateSummary(self,driver,iosTearDown):
        tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
        userSummary = "ios Summary" + tm

        update = UpdateSummary(driver)
        update.update(userSummary)
        assert update.checkUpdateSummary(userSummary)