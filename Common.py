# -*- coding: utf-8 -*-

"""
通用模块，一些供全局使用的模块
"""
import os
import sqlite3 as sql
import platform
import getpass

Linux = 'Linux'
Windows = 'Windows'

# 判断当前操作系统
operatorSystem = platform.system()
# 用户名
operatorUserName = getpass.getuser()

# 数据库及配置文件存放的绝对路径，根据此文件夹判断是否为第一次使用
# 最后程序保留为protable形式，无论放在哪都能运行
dbAbsPath = {'Windows': 'C:\\Users\\%s\\AppData\\Local\\py-password-manager\\' % operatorUserName,
             'Linux': '/home/%s/.py-password-manager/' % operatorUserName}[operatorSystem]

# 用户数据数据库名为管理员stamp
userDataDb = dbAbsPath + 'data.db'
# 管理员密码储存，分为时间戳和key
# 数据表名 admintable
adminDataDb = dbAbsPath + 'admin.db'
admintable = 'admintable'


def is_first_to_use() -> bool:
    """ 是否是第一次使用该程序\n
    1. 查看路径是否存在，不存在则创建一个
    2. 查看用户数据库admin.db是否存在
    3. admin.db中是否有密码
    """
    # 检查文件夹是否存在，不存在则创建一个
    if not os.path.exists(dbAbsPath):
        os.makedirs(dbAbsPath)
        return True
    # 检查管理员验证的数据库是否存在
    if not os.path.exists(adminDataDb):
        return True
    else:
        dbconnect = sql.connect(adminDataDb)
        dbcursor = dbconnect.cursor()
        try:
            # 读取数据库验证信息
            dbcursor.execute('select * from %s' % admintable)
            values = dbcursor.fetchall()
            if len(values) == 0:
                return True
            else:
                return False
        except sql.OperationalError:
            return True
    return False


def get_admin_key():
    DBconnect = sql.connect(adminDataDb)
    DBcursor = DBconnect.cursor()
    try:
        DBcursor.execute('select * from %s' % admintable)
        values = DBcursor.fetchall()
    except sql.OperationalError as e:
        print('get admin key error: ', e)
        return None
    finally:
        DBcursor.close()
        DBconnect.commit()
        DBconnect.close()
    return values[0]


def read_qss(style) -> str:
    try:
        with open(style, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError:
        return ' '
