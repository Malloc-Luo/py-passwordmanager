# -*- coding: utf-8 -*-

"""
通用模块，一些供全局使用的模块
"""
import re
import winreg as wg
import ctypes, sys, os
import sqlite3 as sql
import time

# 管理员密码格式限制
adminPswdFormat = re.compile(r'[0-9a-zA-Z\+\-\*\/\@]{6,256}')

# 数据库及配置文件存放的绝对路径，根据此文件夹判断是否为第一次使用
# 最后程序保留为protable形式，无论放在哪都能运行
dbAbsPath = 'C:\\Users\\%s\\AppData\\Local\\py-password-manager\\' % __import__('getpass').getuser()
userDataDb = dbAbsPath + 'data.db'
# 管理员密码储存，分为时间戳和key
# 数据表名 admintable
adminDataDb = dbAbsPath + 'admin.db'


def is_first_to_use() -> bool:
    """ 是否是第一次使用该程序      
    1. 查看路径是否存在，不存在则创建一个
    2. 查看用户数据库admin.db是否存在
    3. admin.db中是否有密码
    """
    if not os.path.exists(dbAbsPath):
        os.makedirs(dbAbsPath)
        return False

    if not os.path.exists(userDataDb):
        return False
    else:
        dbconnect = sql.connect(userDataDb)
        dbcursor = dbconnect.cursor()

        script1 = """
        select * from admintable
        """
        try:
            dbcursor.execute(script1)
            values = dbcursor.fetchall()
            if len(values) == 0:
                return False
            else:
                return True
        except:
            return False
    return True


def get_admin_password():
    """ 获得管理员密码，也就是用户输入的密码
    """

    return 'Helloworld'


if __name__ == '__main__':
    is_first_to_use()
