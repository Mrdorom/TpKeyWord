# coding:utf-8
from utils.filePath import FilePath
from pageObjects.Android.classAndGrade.imGroup import AddressList


class TestAddFriend(object):
    def testAddFriend(self,driver):
        addresslist = AddressList(driver)
        stedenNumber = ''
        addresslist.update(stedenNumber)
