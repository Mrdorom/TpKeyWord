#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/30 09:59
# @Author : dorom
# @File : setInputMethod.py
# @Software: PyCharm

import os
"""输入法设置"""

def setSougo(emulator):
	commend = "adb -s {0} shell ime set com.sohu.inputmethod.sogou/.SogouIME".format(emulator)
	os.system(commend)

def setUnicodeIME(emulator):
	commend = "adb -s {0} shell ime set io.appium.android.ime/.UnicodeIME".format(emulator)
	os.system(commend)
