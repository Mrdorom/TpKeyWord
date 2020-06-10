#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/30 11:20
# @Author : dorom
# @File : db.py
# @Software: PyCharm


# coding:utf-8
import pymysql

from utils.readYaml import ReadYaml
from utils.filePath import FilePath
from utils.logger import MyLogger


class DbOption(object):
    def __init__(self):
        self.mylogger = MyLogger(self.__class__.__name__).getlogger()
        self.read = ReadYaml()
        btclassDB =  self.read.getStream(FilePath.dbConfigPath)["DB_data"]
        self.host = btclassDB["host"]
        self.username = btclassDB["username"]
        self.password = btclassDB["password"]
        self.port = btclassDB["port"]
        self.basename = btclassDB["basename"]
        self.conn = None

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host,user=self.username,passwd=self.password,db=self.basename,port=self.port,charset='utf8')

        except Exception as msg:
            self.mylogger.info("数据库连接错误：{0}".format(msg))
        return self.conn

    def reconnect(self):
        """
        数据库重连机制
        :return:
        """
        try:
            self.conn.ping()
            return False
        except:
            return self.connect()

    def select(self,sql):
        cursor  = self.connect().cursor()
        try:
            reconnect = self.reconnect()
            if reconnect:
                cursor = reconnect.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as msg:
            self.mylogger.info("sql查询错误：{0}".format(msg)+"\n" + "错误sql:{0}".format(sql))
            data = ()
        cursor.close()
        self.conn.close()
        return data

    def operation(self,sql):
        cursor = self.connect().cursor()
        try:
            reconnect = self.reconnect()
            if reconnect:
                cursor = reconnect.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except Exception as msg:
            self.conn.rollback()
            self.mylogger.info("sql:{0} 操作失败：{1}".format(msg,sql))
        cursor.close()
        self.conn.close()

if __name__ == "__main__":
    sql = "SELECT id FROM bt_course_grouping where id =1000 "
    d = DbOption().select(sql)
    print(d)
    print('ddddddddddddd')

