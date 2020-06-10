#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/10 16:04
# @Author : dorom
# @File : imAdderPage.py
# @Software: PyCharm
from driverOption.baseApi import BaseApi
from pageObjects.iOS.imindexPage import ClassGroup
from utils.readYaml import ReadYaml


class ImAdderPage(object):
    def __init__(self,driver):

        self.readYaml = ReadYaml()
        self.base = BaseApi(driver)
        self.imIndex = ClassGroup(driver)