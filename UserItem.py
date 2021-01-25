# -*- coding: utf-8 -*-

"""
用户密码项目类
用于与数据库、UI交互
"""
import operate_password as op
from Common import get_admin_password

class UserItem(object):
    # 密码明文
    self.plaintext = None
    # 密码密文
    self.ciphertext = None

    def __init__(self, name, account, email_or_phone=None, note=None):
        self.name = name
        self.account = account
        self.email_or_phone = email_or_phone
        self.note = note
