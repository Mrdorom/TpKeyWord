#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/3 09:38
# @Author : dorom
# @File : indexPage.py
# @Software: PyCharm

from utils.readYaml import ReadYaml
from utils.filePath import FilePath
from errorExecption.eleNotFound import EleNotFound
from driverOption.baseApi import BaseApi
import abc


class IndexPage(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self,driver):
		self.driver = driver
		self.readYaml = ReadYaml()
		self.indexPage = self.readYaml.getStream(FilePath.iOSIndexPage)
		self.base = BaseApi(self.driver)

		self.closeAdButton = self.readYaml.getNode(self.indexPage,"closeAdButton")
		self.explorButton = self.readYaml.getNode(self.indexPage,"explorButton")
		self.classButton = self.readYaml.getNode(self.indexPage,"classButton")
		self.learnButton = self.readYaml.getNode(self.indexPage,"learnButton")
		self.questionBankButton = self.readYaml.getNode(self.indexPage,"questionBankButton")
		self.myselfButton = self.readYaml.getNode(self.indexPage,"myselfButton")
		self.navigation = self.readYaml.getNode(self.indexPage,"navigation")

	@abc.abstractmethod
	def switchNavigation(self):
		pass

	def closeAd(self):
		if self.base.iosCheckElement(self.closeAdButton):
			self.base.iosClick(self.closeAdButton)


class Explore(IndexPage):
	def switchNavigation(self):
		self.closeAd()
		if self.base.iosCheckElement(self.explorButton):
			self.base.iosClick(self.explorButton)
		else:
			raise EleNotFound("探索按钮未找到")


class ClassIm(IndexPage):
	def switchNavigation(self):
		self.closeAd()
		if self.base.iosCheckElement(self.classButton):
			self.base.iosClick(self.classButton)
		else:
			raise EleNotFound("班级按钮未找到")


class Learn(IndexPage):
	def switchNavigation(self):
		self.closeAd()
		if self.base.iosCheckElement(self.learnButton):
			self.base.iosClick(self.learnButton)
		else:
			raise EleNotFound("学习中心按钮未找到")


class QuestionBank(IndexPage):
	def switchNavigation(self):
		self.closeAd()
		if self.base.iosCheckElement(self.questionBankButton):
			self.base.iosClick(self.questionBankButton)
		else:
			raise EleNotFound("题库按钮未找到")

class Myself(IndexPage):

	def switchNavigation(self):
		self.closeAd()
		if self.base.iosCheckElement(self.myselfButton):
			self.base.iosClick(self.myselfButton)
		else:
			raise EleNotFound("我的按钮未找到")


class IndexHolder(object):
	def __init__(self,driver):
		self.driver = driver

	def switchNavigation(self,navigation):
		buttonDict= {
			"探索": lambda :Explore(self.driver).switchNavigation(),
			"班级": lambda :ClassIm(self.driver).switchNavigation(),
			"学习中心": lambda :Learn(self.driver).switchNavigation(),
			"题库": lambda :QuestionBank(self.driver).switchNavigation(),
			"我的": lambda :Myself(self.driver).switchNavigation()
		}

		button = buttonDict.get(navigation, False)
		if button:
			button()
		else:
			raise EleNotFound("首页导航类型错误")
