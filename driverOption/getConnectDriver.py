#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/30 14:46
# @Author : dorom
# @File : getConnectDriver.py
# @Software: PyCharm

from errorExecption.driverConnectError import DriverConnectError
import subprocess
import re


def getConnectUdid():
    """
    检查当前连接电脑的手机设备
    :return: 设备udid
    """
    cmd = "adb devices"
    p_str_list = []
    result = subprocess.Popen(cmd,shell=True,stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
    pattern = re.compile(r'b\'(.*?)\\tdevice')
    for daump in result:
        p_str = pattern.findall(str(daump))
        for p in p_str:
            if p:
                p_str_list.append(p)
    if p_str_list:
        return p_str_list
    else:
        raise DriverConnectError("未检测到有设备接入")

def getiOSUdid():
    """
    获取iOS udid
    :return:
    """
    cmd = 'idevice_id -l'
    udid_list = []
    result = subprocess.Popen(cmd,shell=True,stderr =subprocess.PIPE,stdout=subprocess.PIPE ).stdout.readlines()
    pattern = re.compile(r'b\'(.*?)\\n')
    for daump in result:
        p_str = pattern.findall(str(daump))
        for p in p_str:
            if p:
                udid_list.append(p)
    if udid_list:
        return udid_list
    else:
        raise DriverConnectError("未检测到有iOS设备接入")


if __name__ == '__main__':
    getConnectUdid()