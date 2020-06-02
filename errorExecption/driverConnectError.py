#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/30 15:34
# @Author : dorom
# @File : driverContentError.py
# @Software: PyCharm

class DriverConnectError(Exception):
    pass

class DriverUdidNotExit(Exception):
    """
    手机设备信息不存在
    """
    pass
