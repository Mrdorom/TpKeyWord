# coding:utf-8
from driverOption.baseApi import BaseApi
from utils.filePath import FilePath
from utils.readYaml import ReadYaml
from pageObjects.Android.loginPage import LoginPage
import abc


class ImGroup(object):

    __metaclass__ = abc.ABCMeta
    def __init__(self,driver):
        self.readYaml = ReadYaml()
        self.base = BaseApi(driver)

        #校园页面
        self.schoolNavigationBar = self.readYaml.getStream(FilePath.androidIndexPage)
        self.schoolclass =self.readYaml.getNode(self.schoolNavigationBar,'class')

        #获取通讯录元素路径
        self.imGroup = self.readYaml.getStream(FilePath.androidGroup)
        #通讯录页面
        self.addressList = self.readYaml.getNode(self.imGroup,'addressList')
        #添加好友页面
        self.addFriend = self.readYaml.getNode(self.imGroup,'addFriend')
        #添加好友输入框
        self.addFriendScanf = self.readYaml.getNode(self.imGroup,'addFriendScanf')
        #添加好友按钮
        self.addFriendButton = self.readYaml.getNode(self.imGroup,'addFriendButton')
        #添加好友验证按钮
        self.sendFriendButton = self.readYaml.getNode(self.imGroup,'sendFriendButton')





    @abc.abstractmethod
    def update(self,*args,**kwargs):
        pass

class AddressList(ImGroup):

    def update(self,studentNumber):
        self.base.click(self.schoolclass)
        self.base.click(self.addressList)
        self.base.sendKeys(self.addFriend,studentNumber)
        self.base.click(self.addFriendButton)
        self.base.click(self.sendFriendButton)


    def checkUpdateRes(self,studenNumber,password):
        login = LoginPage
        login.login(studenNumber,password)
        self.base.click(self.schoolclass)