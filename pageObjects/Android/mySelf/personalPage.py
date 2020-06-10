# coding:utf-8


import abc
from driverOption.baseApi import BaseApi
from errorExecption.eleNotFound import EleNotFound
from utils.filePath import FilePath # 配置文件路径
from utils.readYaml import ReadYaml # 获取元素
from utils.logger import MyLogger
from pageObjects.Android.indexPage import  MySelf
from pageObjects.Android.loginPage import LoginPage


class PersonalHolder(object):
    __mateclass__ = abc.ABCMeta

    def __init__(self,driver):
        self.logger = MyLogger(self.__class__.__name__).getlogger()
        self.driver = driver
        self.base = BaseApi(self.driver)
        self.readYaml =  ReadYaml()
        self.mySelf = MySelf(self.driver)
        # 我的页面
        self.userInfoPage = self.readYaml.getStream(FilePath.androidUserInfoPage)
        # 个人资料按钮
        self.personalCenter = self.readYaml.getNode(self.userInfoPage,"personalCenter")
        #获取我的页面当前用户名
        self.userName = self.readYaml.getNode(self.userInfoPage,'userName')

        # 个人资料页面
        self.personalPage = self.readYaml.getStream(FilePath.androidPersonalPage)
        self.updateNameButton = self.readYaml.getNode(self.personalPage,"updateNameButton")
        self.updateNameInputButton = self.readYaml.getNode(self.personalPage,"updateNameInputButton")
        self.updateNameSaveButton = self.readYaml.getNode(self.personalPage,"updateNameSaveButton")
        #返回
        self.backButton = self.readYaml.getNode(self.personalPage,"backButton")

        #修改密码
        self.updatePasswdButton = self.readYaml.getNode(self.personalPage, "updatePasswdButton")
        self.oldPasswordFild = self.readYaml.getNode(self.personalPage, "oldPasswordFild")
        self.newPasswordFild = self.readYaml.getNode(self.personalPage, "newPasswordFild")
        self.affirePasswordFild = self.readYaml.getNode(self.personalPage, "affirePasswordFild")
        self.savePassword = self.readYaml.getNode(self.personalPage, "savePassword")

        #修改学校
        self.schoolButton = self.readYaml.getNode(self.personalPage,"schoolButton")
        self.schoolFile = self.readYaml.getNode(self.personalPage,"schoolFile")
        self.schoolNameText = self.readYaml.getNode(self.personalPage,"schoolNameText")

        #修改简介
        self.updateSummaryButton = self.readYaml.getNode(self.personalPage,"updateSummaryButton")
        self.newSummaryFild = self.readYaml.getNode(self.personalPage, "newSummaryFild")
        self.newSummaryText = self.readYaml.getNode(self.personalPage, "newSummaryText")

        #修改工作单位
        self.workButton = self.readYaml.getNode(self.personalPage, "workButton")
        self.workFild = self.readYaml.getNode(self.personalPage, "workFild")
        self.workNameText = self.readYaml.getNode(self.personalPage, "workNameText")



    @abc.abstractmethod
    def update(self,*args,**kwargs):
        pass


#修改用户名
class UpdateUserName(PersonalHolder):

    def update(self,userName):
        """
        2、 点击个人资料
        3、 修改用户
        :return:
        """
        self.mySelf.chooseNavigation()
        self.base.click(self.personalCenter)
        self.base.click(self.updateNameButton)
        self.base.sendKeys(self.updateNameInputButton,userName)
        self.base.click(self.updateNameSaveButton)
        self.base.click(self.readYaml.getNode(self.personalPage,"backButton"))


    def checkUpdateRes(self,userName):

        destText = self.base.getText(self.userName)
        print('------------------------------------------------------------:'+destText)
        self.logger.info("获取到的用户名：{0}".format(destText))
        if destText == userName:
            return True
        else:
            return False


#修改学校名称
class UpdateSchoolName(PersonalHolder):
    def update(self,schoolName):
        self.mySelf.chooseNavigation()
        self.base.supperElement(self.personalCenter, "进入个人中心页面失败")
        self.base.click(self.personalCenter)
        self.base.click(self.schoolButton)
        self.base.sendKeys(self.schoolFile, schoolName)
        self.base.click(self.updateNameSaveButton)
        self.base.click(self.readYaml.getNode(self.personalPage, "backButton"))

    def checkUpdateRes(self, schoolName):
        self.base.click(self.personalCenter)
        destText = self.base.getText(self.schoolNameText)
        self.logger.info("获取到的用户名：{0}".format(destText))
        if destText == schoolName:
            return True
        else:
            return False


class UpdateChangePassword(PersonalHolder):
    def update(self,password,new_password):
        self.mySelf.chooseNavigation()
        self.base.supperElement(self.personalCenter,'进入个人中心页面失败')
        self.base.click(self.personalCenter)
        self.base.click(self.updatePasswdButton)
        self.base.sendKeys(self.oldPasswordFild,password)
        self.base.sendKeys(self.newPasswordFild,new_password)
        self.base.sendKeys(self.affirePasswordFild,new_password)
        self.base.click(self.savePassword)

    def checkUpdateRes(self, user_id,password):
        LoginPage(self.driver).login(user_id,password)


class UpdateChangeIntroduction(PersonalHolder):
    def update(self,introduction):
        self.mySelf.chooseNavigation()
        self.base.supperElement(self.personalCenter, '进入个人中心页面失败')
        self.base.click(self.personalCenter)
        self.base.click(self.updateSummaryButton)
        self.base.sendKeys(self.newSummaryFild,introduction)
        self.base.click(self.updateNameSaveButton)

    def checkUpdateRes(self, introdoction):
        # self.base.click(self.personalCenter)
        destText = self.base.getText(self.newSummaryText)
        self.logger.info("获取到的用户名：{0}".format(destText))
        if destText == introdoction:
            return True
        else:
            return False

    class UpdateChangeWorkName(PersonalHolder):
        def update(self, workName):
            self.mySelf.chooseNavigation()
            self.base.supperElement(self.personalCenter, '进入个人中心页面失败')
            self.base.click(self.personalCenter)
            self.base.click(self.workButton)
            self.base.sendKeys(self.workFild, workName)
            self.base.click(self.updateNameSaveButton)

        def checkUpdateRes(self, introdoction):
            # self.base.click(self.personalCenter)
            destText = self.base.getText(self.workNameText)
            self.logger.info("获取到的用户名：{0}".format(destText))
            if destText == introdoction:
                return True
            else:
                return False