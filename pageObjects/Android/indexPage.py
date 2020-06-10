#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/2 19:16
# @Author : dorom
# @File : indexPage.py
# @Software: PyCharm

from utils.filePath import FilePath
from utils.logger import MyLogger
from utils.readYaml import ReadYaml
from driverOption.baseApi import BaseApi
from errorExecption.eleNotFound import EleNotFound


class IndexPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.base = BaseApi(self.driver)
        self.readyaml = ReadYaml()
        self.indexPage = self.readyaml.getStream(FilePath.androidIndexPage)


        self.explore = self.readyaml.getNode(self.indexPage,"explore")
        self.classTab= self.readyaml.getNode(self.indexPage,"class")
        self.reconnetButton = self.readyaml.getNode(self.indexPage,"reconnetButton")
        self.questionBank = self.readyaml.getNode(self.indexPage,"questionBank")
        self.myStudy = self.readyaml.getNode(self.indexPage,"myStudy")
        self.mySelf = self.readyaml.getNode(self.indexPage,"mySelf")
        print(self.mySelf)

    def comeNATIVEAPP(self):
        """切换到原生"""
        self.base.switchContext("NATIVE_APP")


    def chooseNavigation(self):
        pass


class Explore(IndexPage):

    def chooseNavigation(self):
        if self.base.checkElement(self.explore):
            self.base.click(self.explore)
        else:
            raise EleNotFound("探索按钮未找到")


class ClassIm(IndexPage):

    def chooseNavigation(self):
        if self.base.checkElement(self.classTab):
            self.base.click(self.classTab)
        else:
            raise EleNotFound("班级按钮未找到")


class Learn(IndexPage):

    def chooseNavigation(self):
        if self.base.checkElement(self.myStudy):
            self.base.click(self.myStudy)
        else:
            raise EleNotFound("学习中心按钮未找到")



class QuestionBank(IndexPage):

    def chooseNavigation(self):
        if self.base.checkElement(self.questionBank):
            self.base.click(self.questionBank)
        else:
            raise EleNotFound("题库按钮未找到")


class MySelf(IndexPage):

    def chooseNavigation(self):
        if self.base.checkElement(self.mySelf,180):
            self.base.click(self.mySelf)
        else:
            raise EleNotFound("我的按钮未找到")
