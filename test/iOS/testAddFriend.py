#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/11 18:25
# @Author : dorom
# @File : testAddFriend.py
# @Software: PyCharm


from pageObjects.iOS.imAddressPage import ApplyFriend


class TestAddFriend(object):
    def testAddFritend(self,driver,db,classGroupSetUp,classGroupTearDown,iosTearDown):

        a = ApplyFriend(driver,db)
        a.addFirend('2004000019')
        assert a.checkAddResult(1000023,1000944)
