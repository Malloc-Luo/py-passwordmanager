# -*- coding: utf-8 -*-

"""
通用模块，一些供全局使用的模块
"""
import re
import winreg as wg

# 管理员密码格式限制
adminPswdFormat = re.compile(r'[0-9a-zA-Z\+\-\*\/\@]{6,256}')

# 数据库及配置文件存放的绝对路径，根据此文件夹判断是否为第一次使用
# 最后程序保留为protable形式，无论放在哪都能运行
dbAbsPath = 'C:\\Users\\%s\\AppData\\Local\\py-password-manager\\' % __import__('getpass').getuser()


def get_admin_password():
    """ 获得管理员密码，也就是用户输入的密码
    """
    return 'Helloworld'


