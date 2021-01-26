# -*- coding: utf-8 -*-

"""
用户密码项目类
用于与数据库、UI交互
"""
import operate_password as op
from Common import get_admin_password

class UserItem(object):
    def __init__(self, ID, name, account, email_or_phone=None, note=None):
        self.id = ID
        self.name = name
        self.account = account
        self.email_or_phone = email_or_phone
        self.note = note
        # 密码明文
        self.plaintext = None
        # 密码密文
        self.ciphertext = None

    def load_plaintext(self, pswd):
        self.plaintext = pswd
        self.ciphertext = op.encrypt_password(self.plaintext, get_admin_password())
        return self

    def load_ciphertext(self, pswd):
        self.ciphertext = pswd
        self.plaintext = op.decrypt_password(self.ciphertext, get_admin_password())
        return self

    def __str__(self):
        return ('id: %s\nname: %s\naccount: %s\nplaintext: %s\nciphertext: %s\nemail/phone: %s\nnote: %s\n' 
                % (self.id, self.name, self.account, self.plaintext, self.ciphertext, self.email_or_phone, self.note))
