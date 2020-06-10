#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/27 15:37
# @Author : dorom
# @File : baseApi.py
# @Software: PyCharm
import os
from selenium.webdriver.support.select import Select
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from errorExecption.eleNotFound import EleNotFound
from utils.logger import MyLogger
import time


class BaseApi(object):
    def __init__(self,driver):
        self.driver = driver
        self.logger = MyLogger(self.__class__.__name__).getlogger()

    def checkElement(self,loc,time=5):
        """
        检查元素是否存在
        :param loc: loc type is tuple
        :return: check result
        """
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_element(*loc))
            return True
        except:
            return False


    def checkElements(self,loc,time=10):
        """
        检查元素是否存在
        :param loc: loc type is tuple
        :return: check result
        """
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_elements(*loc))
            return True
        except:
            return False

    def findElement(self, loc, timeout=5):
        """
        查找单个元素
        :param loc: id,kw
        :param timeout: 超时时间
        :return: Element
        """
        if self.checkElement(loc, timeout):
            return self.driver.find_element(*loc)
        else:
            self.logger.error("元素：{0} 查找失败".format(loc))
            raise EleNotFound("{0} 元素列表未找到".format(loc))

    def findElements(self, loc, timeout=5):
        """
        查找多个元素
        :param loc: id,kw
        :param timeout: 超时时间
        :return: Element LIst
        """
        if self.checkElement(loc, timeout):
            return self.driver.find_elements(*loc)
        else:
            self.logger.error("元素：{0} 查找失败".format(loc))
            raise EleNotFound("{0} 元素列表未找到".format(loc))


    def findElementUiautomator(self, loc):
        """
        使用uiuatomator定位元素 Android专用
        :param loc:  new UiSelector().text("id")
        :return:  Element
        """

        self.logger.info(str(('正在使用 new UiSelector().{0}(\"{1}\")'.format(loc[0], loc[1]))))
        try:
            EleRes = self.driver.find_element_by_android_uiautomator \
                ('new UiSelector().{0}(\"{1}\")'.format(loc[0], loc[1]))
            return EleRes
        except:
            self.logger.error("元素：{0} 查找失败".format(loc))
            raise EleNotFound("findElementUiautomator Error")

    def checkAccessiblity(self, loc, timeout=10):
        """
        Accessiblity 检查元素是否存在
        :param loc: accessibility Id
        :param timeout: 超时时间
        :return: Element
        """
        try:
            WebDriverWait(self.driver, timeout).until(lambda x: x.find_element_by_accessibility_id(loc))
            return True
        except:
            return False

    def findAccessiblity(self, loc, timeout=10):
        """
        accessibility Android 使用的是 content-desc
        属性 IOS使用的是 accessibility identifier属性
        :param loc:
        :param timeout:
        :return:
        """
        if self.checkAccessiblity(loc, timeout):
            ele = self.driver.find_element_by_accessibility_id(loc)
            return ele
        else:
            self.logger.error("元素：{0} 查找失败".format(loc))
            raise EleNotFound("findAccessiblity find element error ")

    def iosPredicates(self, ele, timeout=5):
        """
        查找多个元素  iOS 专用
        :param ele:
        :param timeout:
        :return:
        """
        if self.iosCheckElements(ele, timeout):
            ele = self.driver.find_elements_by_ios_predicate(ele)
            return ele
        else:
            raise EleNotFound("iOS ios_predicates：{} 元素未找到".format(ele))

    def iosPredicate(self, ele, timeout=5):
        """
        查找单个元素 iOS专用
        :param ele:
        :param timeout:
        :return:
        """
        if self.iosCheckElement(ele, timeout):
            ele = self.driver.find_element_by_ios_predicate(ele)
            return ele
        else:
            raise EleNotFound("iOS ios_predicate：{} 元素未找到".format(ele))

    def iosCheckElement(self, ele, timeout=5):
        """
        检查 iOS 单个元素是否存在
        :param ele:
        :param timeout:
        :return:
        """
        findFlage = True
        while findFlage and timeout > 0:
            try:
                self.driver.find_element_by_ios_predicate(ele)
                return True
            except:
                pass
            timeout -= 0.5
            if timeout == 0:
                return False

    def iosCheckElements(self, ele, timeout=10):
        """
        检查 ios 多个元素是否存在
        :param ele:
        :param timeout:
        :return:
        """
        findFlage = True
        while findFlage and timeout>0:
            try:
                self.driver.find_element_by_ios_predicate(ele)
                return True
            except:
                pass
            timeout -=0.5
            if timeout==0:
                return False

    def Select(self, loc):
        """
        Select 下拉框
        :param loc:
        :return:
        """
        s = Select(self.findElement(loc))
        return s

    def click(self, *loc):
        """
        点击操作
        :param loc:
        """
        self.findElement(*loc).click()


    def getText(self, loc):
        """
        获取元素text文本
        :param loc: 元素
        :return:
        """
        textData = self.findElement(loc,10).text
        return textData

    def iosClick(self,loc,timeout=5):
        """
        ios 点击元素
        :param loc:
        :return:
        """
        self.iosPredicate(loc,timeout).click()


    def setValue(self,loc, params,lenth=10):
        """
        ios 输入值
        :param ele:  元素
        :param params:  输入值
        :param lenth:  清除次数
        :return:
        """

        destEle = self.iosPredicate(loc)
        destEle.click()
        self.iosClearText(lenth)
        destEle.set_value(params)

    def iosClearText(self, lenth):
        """
        ios 使用键盘删除 输入框内的数据
        :param lenth: 删除的次数
        """
        if lenth:
            try:
                ele_button = 'type=="XCUIElementTypeKey" and label=="删除"'
                ele = self.iosPredicate(ele_button,5)
            except:
                ele_button = 'type=="XCUIElementTypeKey" and label=="delete"'
                ele = self.iosPredicate(ele_button, 5)

            for l in range(lenth):
                ele.click()

    def sendKeys(self, loc, text):
        """
        输入
        :param loc: 元素
        :param text: 文本
        :return:
        """
        ele = self.findElement(loc)
        ele.clear()
        ele.send_keys(text)

    def back(self):
        """
        键盘返回
        :return:
        """
        self.driver.keyevent(4)

    def getSize(self):
        """
        获取窗口大小
        :return: x轴、y轴坐标
        """
        are = self.driver.get_window_size()
        x = are['width']
        y = are['height']
        return x, y

    def getPage(self):
        """
        获取当前的 source Page
        :return: page
        """
        page = self.driver.page_source
        return page

    def opterioneycode(self, keycode, metastate=None):
        """
            键盘输入
            具体请看文档： https://blog.csdn.net/weixin_40180628/article/details/79169846
        """
        self.driver.press_keycode(keycode, metastate)


    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        从一个坐标移动到另一个坐标
        :param start_x: 起始x坐标
        :param start_y: 起始y坐标
        :param end_x:  结束X 坐标
        :param end_y: 结束Y坐标
        :param duration:
        :return:
        """
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)


    def androidap(self,udid,x,y):
        """
        Android adb 命令点击坐标
        :param udid: 手机udid
        :param x: 横坐标
        :param y: 纵坐标
        :return:
        """
        os.popen('adb -s {0} shell input tap {1} {2}'.format(udid, x, y))

    def iosap(self, x, y):
        """
        ios tap 方法
        :return:
        """
        are = self.driver.get_window_size()
        x = int(float(x / are["width"]) * are["width"])
        y = int(float(y / are["height"]) * are["height"])
        self.driver.execute_script("mobile: tap", {"x": x, "y": y, "duration": 500})

    def touch(self, x, y, x1, y1):
        """
        触摸移动
        :param x:
        :param y:
        :param x1:
        :param y1:
        :return:
        """
        TouchAction(self.driver).press(x=x, y=y).move_to(x=x1, y=y1).release().perform()

    def swipeUp(self, x_num=0.5, y1_num=0.25, y2_num=0.75, time=1000):
        """
        屏幕上滑
        :param x_num:
        :param y1_num:
        :param y2_num:
        :param time:
        :return:
        """
        are = self.getSize()
        x = int(are[0] * x_num)
        y1 = int(are[1] * y1_num)
        y2 = int(are[1] * y2_num)
        self.swipe(x, y1, x, y2, time)

    def swipeDown(self, x_num=0.5, y1_num=0.75, y2_num=0.25, time=1000):
        """
        屏幕下滑
        :param x_num:
        :param y1_num:
        :param y2_num:
        :param time:
        :return:
        """
        are = self.getSize()
        x = int(are[0] * x_num)
        y1 = int(are[1] * y1_num)
        y2 = int(are[1] * y2_num)
        self.swipe(x, y1, x, y2, time)

    def swipeRight(self, time=500):
        """
        屏幕右滑
        :param time:
        :return:
        """
        are = self.getSize()
        x1 = int(are[0] * 0.1)
        x2 = int(are[0] * 0.9)
        y = int(are[1] * 0.5)
        self.swipe(x1, y, x2, y, time)

    def swipeLeft(self, x_num=0.1, y1_num=0.5, x2_num=0.9, time=500):
        """
        屏幕左滑
        :param x_num:
        :param y1_num:
        :param x2_num:
        :param time:
        :return:
        """
        are = self.getSize()
        x1 = int(are[0] * x_num)
        x2 = int(are[0] * x2_num)
        y = int(are[1] * y1_num)
        self.swipe(x2, y, x1, y, time)

    def moveTo(self, loc):
        """
        鼠标移动到元素ele
        :param loc:
        :return:
        """
        ele = self.findElement(loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def scroll(self,ele1,ele2):
        """
        从ele1 滑动到ele2
        :param ele1:
        :param ele2:
        :return:
        """
        self.driver.scroll(ele1,ele2)


    def getAllContext(self):
        """
        获取所有的Context
        :return:
        """
        contexts = self.driver.Contexts
        self.logger.info("当前所有的contexts: {0}".format(contexts))
        return contexts

    def getCurrentContext(self):
        """
        获取当前窗口 context
        :return:
        :return:
        """
        currentContext = self.driver.current_context
        self.logger.info("当前Context: {0}".format(currentContext))
        return self.driver.current_context

    def switchContext(self,context):
        """
        切换到指定的context 上
        :param context:
        :return:
        """
        self.driver._switch_to.context(context)

    def getAllHandles(self):
        """
        获取所有的窗口的handles
        :return:
        """
        allHandles = self.driver.window_handles
        return allHandles

    def switchHandles(self,handles):
        """
        切换到指定的headles
        :param handles: 需啊哟切换的hadles
        :return:
        """
        self.driver._switch_to.window(handles)

    def switchToFrame(self, loc):
        """frame 窗口切换"""
        self.driver.switch_to.frame(loc)