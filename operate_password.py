# -*- coding: utf-8 -*-
"""
保存在数据库中的密码需要进行加密处理，具体如下：
1. 生成输入密码的sha256，并且拆分成256个整数，作为密钥
2. 计算需要保存密码的长度，不够256则随机插入空格字符，补充至256
3. 将转换后的密码字符转换成对应asiic值，与密钥进行异或运算
4. 得到的结果根据asiic表转换成字符合成字符串作为密文
5. 解码时执行1~4操作，但2需要保存密码换成密文
"""
from hashlib import sha256
from random import randint
from functools import reduce


def insert_random_space(s: str, length: int) -> str:
    """ 向字符串中插入随机空格至指定长度
    Args:
        s: 输入字符串
        length: 指定填充后长度
    Returns:
        填充至指定长度的字符串
    """
    ls = list(s)
    while len(ls) < length:
        ls.insert(randint(0, len(ls)), '\t')
    return ''.join(ls)


def encrypt_password(pswdtext: str, keytext: str) -> str:
    """ 加密密码
    Args:
        pswdtext: 需要被加密的密码
        keytext: 作为key的密码，也就是登录时用的密码
    Returns:
        加密后的密文
    """
    # sha256
    keyhash = sha256(keytext.encode('utf-8')).hexdigest()
    key = [int(c, 16) for c in keyhash]
    # 插入空格补充至key等长
    pswds = insert_random_space(pswdtext, len(key))
    pswdsList = [ord(c) for c in pswds]
    # 异或加密
    encryptText = list(map(lambda x, y: x ^ y, pswdsList, key))
    # 转换成字符串返回
    return reduce(lambda x, y: x + y, [chr(i) for i in encryptText])


def decrypt_password(encryptText: str, keytext: str) -> str:
    """ 根据key密码解码
    Args:
        encryptText: 密文
        keytext: 作为key的密码，也就是登录时用的密码
    Returns:
        解码后的密码
    """
    keyhash = sha256(keytext.encode('utf-8')).hexdigest()
    key = [int(c, 16) for c in keyhash]

    encryptTextList = [ord(c) for c in encryptText]
    decryptText = list(map(lambda x, y: x ^ y, encryptTextList, key))
    # 去掉中间的空格
    return reduce(lambda x, y: x + y, [chr(i) for i in decryptText]).replace('\t', '')
