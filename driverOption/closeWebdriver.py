#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/26 22:26
# @Author : dorom
# @File : closeWebdriver.py
# @Software: PyCharm


import subprocess,os,re


class CloseWebdriver(object):

    def closeWebdriver(self,webdriver):
        """
        # chromedriver_71_73
        关闭chrome Driver 驱动
        :param webdriver:
        :return:
        """
        cmd = 'ps -ef |grep {0}'.format(webdriver)
        pid_list = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        pattrn = re.compile(r"(\d+)")
        for pid in pid_list:
            cmd = 'kill -9 {0}'.format(pattrn.findall(str(pid))[0])
            os.system(cmd)