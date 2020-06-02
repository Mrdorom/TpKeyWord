#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/25 14:56
# @Author : dorom
# @File : readYaml.py
# @Software: PyCharm

import yaml

from errorExecption.nodeError import NodeError
from errorExecption.openFileError import OpenFileError


class ReadYaml(object):

    def __init__(self):
        self.file = None

    def getStream(self,path):
        """
        打开yaml文件，读取数据流
        :param path: yaml 文件地址
        """
        self.file = path
        try:
            with open(path,encoding="utf-8") as file:
                stream = yaml.full_load(file.read())
                return stream
        except :
            raise OpenFileError("打开文件:{0}错误".format(path))

    def getNode(self,stream,nodeName):
        """
        读取yaml 节点数据
        :param nodeName: 节点名称
        :return: 节点数据
        """
        if stream:
            nodeValue = stream.get(nodeName,False)
            if nodeValue:
                type = nodeValue.get("type",False)
                element = nodeValue.get("element",False)
                if type is None or type is False:
                    return element
                else:
                    return type,element
            else:
                raise NodeError("文件：{0}，没有数据节点:{1}".format(self.file,nodeName))
        else:
            raise  NodeError("文件：{0}的yaml，读取节点:{1} 错误".format(self.file,nodeName))
