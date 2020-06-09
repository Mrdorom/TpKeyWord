#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/6/9 10:53
# @Author : dorom
# @File : iOSRun.py.py
# @Software: PyCharm


from utils.filePath import FilePath
from utils.readYaml import ReadYaml
from driverOption.appiumServer import AppiumServer
from driverOption.getConnectDriver import getiOSUdid
from errorExecption.driverConnectError import DriverUdidNotExit
import pytest
import multiprocessing


class IosRun(object):
    def __init__(self):
        self.path = FilePath()
        self.yaml = ReadYaml()

    def startAppiumServer(self,data):
        """
        pytest 使用外部 driverDict 参数 启动 Appium server
        :param data: driverDict
        :return:
        """
        driverName= data["deviceName"]
        pytest.main(["-s", "--driverDict={0}".format(data), "--html={0}/{1}.html".format(FilePath.reportPath,driverName),"{0}".format(FilePath.iOSTestDir)])

    def main(self):
        """
        iOS 测试入口方法， 根据连接的手机设备启动AppiumServer
        1、读取所有手机配置信息
        2、检查已经连接电脑的手机设备的udid
        3、获取已连接设备的配置信息
        4、启动Appium 设备
        :return:
        """
        driverConfigPath = self.path.androidDriverPath
        driverData = self.yaml.getStream(driverConfigPath)

        connetcDriver = getiOSUdid()

        desired_pool = []
        for udid in connetcDriver:
            if udid not in driverData:
                DriverUdidNotExit("配置文件没有设备：{0}的信息".format(udid))

            for data in driverData:
                if data["udid"] == udid:
                    break

            udid = data["udid"]
            host = data["host"]
            port = data["port"]
            server = AppiumServer(host, port, udid)
            server.startAppiumServer()

            pool = multiprocessing.Process(target=self.startAppiumServer, args=(data,))
            desired_pool.append(pool)

        for pool in desired_pool:
            pool.start()

        for pool in desired_pool:
            pool.join()


if __name__ == '__main__':
    runFunc = IosRun()
    runFunc.main()