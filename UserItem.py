# -*- coding: utf-8 -*-

"""
用户密码项目类
用于与数据库、UI交互
"""
import operate_password as op
from Common import get_admin_password

class UserItem(object):
    def __init__(self, ID, name, account, 
                    password=None, email_or_phone=None, note=None,
                    _plainpswd=None):
        self.id = ID
        self.name = name
        self.account = account
        self.email_or_phone = email_or_phone
        self.note = note
        # 这里的密码是密文，加载明文密码请直接使用 load_plaintext函数
        self.password = password
        self._plainpswd = _plainpswd

        if not ((self.password is None) ^ (self._plainpswd is None)):
            raise ValueError('密文和明文在初始化时有且仅有一个为有效') 

    def load_key(self, key):
        if self._plainpswd is not None:
            self.password = op.encrypt_password(self._plainpswd, key)
            self._plainpswd = None
        return self

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < 6:
                return [self.id, self.name, self.account, self.password, self.email_or_phone, self.note][index]
            else:
                raise IndexError('超出索引范围，数值索引为 0 ~ 6')
        elif isinstance(index, str):
            try:
                return {'id': self.id, 
                        'name': self.name, 
                        'account': self.account, 
                        'password': self.password, 
                        'email_or_phone': self.email_or_phone,
                        'note': self.note}[index]
            except:
                raise IndexError('\'%s\' 不是UserItem的属性' % index)
        else:
            raise TypeError('索引是 int 或 str')

    def __setitem__(self, index, value):
        if isinstance(index, (str)):
            if index in {0, 'id'}:
                self.id = value
            elif index in {1, 'name'}:
                self.name = value
            elif index in {2, 'account'}:
                self.account = value
            elif index in {3, 'password'}:
                self.password = value
            elif index in {4, 'email_or_phone'}:
                self.email_or_phone = value
            elif index in {5, 'note'}:
                self.note = value
            else:
                raise IndexError('没有索引 \'%s\'' % index)
        else:
            raise TypeError('索引的类型为 int 或 str')

    def __str__(self):
        return ('id: %s\nname: %s\naccount: %s\npassword: %s\nemail/phone: %s\nnote: %s\n'
                % (self.id, self.name, self.account, self.password, self.email_or_phone, self.note))


if __name__ == '__main__':
    user = UserItem('12345', '1231', '24230', '******', '465456', '4654')
    print(user['name'])
    print(user)
