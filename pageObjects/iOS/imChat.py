#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/11 14:52
# @Author : dorom
# @File : imChat.py
# @Software: PyCharm


import abc

from driverOption.baseApi import BaseApi
from utils.readYaml import ReadYaml


class Chat(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self,driver):
        self.readYaml = ReadYaml()
        self.base = BaseApi(driver)

    @abc.abstractmethod
    def chat(self,content,pic,meme):
        """
        聊天
        :param content:  消息文本内容
        :param pic:  图片
        :param meme: 表情
        :return:
        """
        pass

    @abc.abstractmethod
    def updateClassGroupRemarks(self,remark):
        """
        修改群名片
        :param remark:
        :return:
        """
        pass

    @abc.abstractmethod
    def announce(self,annouce):
        """
        发布公告
        :param annouce: 公告内容
        :return:
        """
        pass


class Announce(Chat):
    def chat(self, content, pic, meme):
        pass

    def updateClassGroupRemarks(self, remark):
        pass

    def clickAnnouce(self):
        """
        不同的账号点击编辑群公告按钮
        :return:
        """
        pass

    def announce(self, annouce):
        self.clickAnnouce()


    def checkStudentReseleNoticePermission(self):
        """
        校验学员发布公告权限
        :return:
        """
        pass

