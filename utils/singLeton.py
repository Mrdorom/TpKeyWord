#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/25 18:32
# @Author : dorom
# @File : singLeton.py
# @Software: PyCharm
from functools import wraps

def singLeton(cls):
    """
    类装饰器
    :param cls: 装饰类
    :return:
    """
    __instance = {}

    def getInstance(*args,**kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args,**kwargs)
        return __instance[cls]
    return getInstance