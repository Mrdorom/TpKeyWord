# coding:utf-8

from pageObjects.Android.mySelf.personalPage import UpdateUserName,UpdateSchoolName,UpdateChangePassword,UpdateChangeIntroduction

import  pytest
from utils.filePath import FilePath
from utils.readYaml import ReadYaml
import time
from utils.filePath import FilePath
from utils.readYaml import ReadYaml

##修改用户名
# class TestPersonal(object):
#
#     def testUpdateName(self,driver,driverFunc):
#         tm = time.strftime("%H:%M:%S",time.localtime(time.time()))
#         userName = '巴啦啦'
#         userName = userName + str(tm)
#         updateName = UpdateUserName(driver)
#         updateName.update(userName)
#         assert updateName.checkUpdateRes(userName)

## 修改学校
# class TestSchool(object):
#     def testSchoolName(self,driver,driverFunc,schoolName = '清华大学'):
#         tm = time.strftime("%H:%M:%S",time.localtime(time.time()))
#         schoolName = schoolName + str(tm)
#         updateChoole = UpdateSchoolName(driver)
#         updateChoole.update(schoolName)
#         assert updateChoole.checkUpdateRes(schoolName)

# #修改密码
# class TestChangePassword(object):
#
#     def testcChangePassword(self,driver,driverFunc):
#         updateChangePassword = UpdateChangePassword(driver)
#         readYaml = ReadYaml()
#         user = readYaml.getStream(FilePath.androidLoginParams)
#         passWord = user[0]["password"]
#         new_password = 'a1234567'
#         updateChangePassword.update(passWord,new_password)
#         user_id =  user[0]["account"]
#         updateChangePassword.checkUpdateRes(user_id,new_password)
#         updateChangePassword.update(new_password,passWord)
#         updateChangePassword.checkUpdateRes(user_id, passWord)
#         time.sleep(5)

# #修改简介
# class TestChangeIntroduction(object):
#
#     def testChangeIntroduction(self,driver,driverFunc,introduction = '本是青灯不归客，却因浊酒恋红尘'):
#         tm = time.strftime("%H:%M:%S",time.localtime(time.time()))
#         introduction = introduction + str(tm)
#         updateChoole = UpdateChangeIntroduction(driver)
#         updateChoole.update(introduction)
#         assert updateChoole.checkUpdateRes(introduction)
#         print('简介修改成功')

##修改工作单位
# class TestChangWorkName(object):
#     def testChangeIntroduction(self,driver,driverFunc,workName = '银河'):
#         tm = time.strftime("%H:%M:%S", time.localtime(time.time()))
#         workName = workName + str(tm)
#         updateChoole = UpdateChangeIntroduction(driver)
#         updateChoole.update(workName)
#         assert updateChoole.checkUpdateRes(workName)
#         print('工作单位修改成功')