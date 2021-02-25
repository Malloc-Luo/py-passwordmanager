# -*- coding:utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal
from Setting import Setting
from UserItem import UserItem
from Common import dbAbsPath, userDataDb
import sqlite3 as sql
import re
import time
import shutil
import os


class DataBase(QObject):
    # 发送UserItem对象的字典
    sendUserItemsSignal = pyqtSignal(dict)
    # 筛选结果信号
    filiteResSignal = pyqtSignal(list)
    # 删除结果的信号
    deleteItemSignal = pyqtSignal(bool, str)
    # 添加结果的信号
    addItemSignal = pyqtSignal(bool, UserItem)
    # 修改信号，修改后把原信息发回去
    modifySignal = pyqtSignal(bool, str, str, str)

    def __init__(self):
        super().__init__()
        self.dbcon = None
        self.dbcur = None
        # 是否连接到了数据库
        self.isConnectToDB = False
        # 备份数据库标志，如果允许备份且没有备份则备份，之后清空
        self.backupDatabaseFlag = False
        self.get_db_name('')

    def __del__(self):
        if self.isConnectToDB is True:
            self.dbcur.close()
            self.dbcon.commit()
            self.dbcon.close()

    def backup_database(self):
        path = dbAbsPath + 'backup'
        if os.path.exists(path) is False:
            os.makedirs(path)
        shutil.copyfile(userDataDb, dbAbsPath + 'backup\\%s.db.bk' % str(int(time.time()))[-10:])

    def check_table_exists(self):
        """ 检查数据表data.db是否存在
        """
        # 检查数据表是否存在，不存在则创建一个
        self.dbcur.execute('''create table if not exists
                            userdata(id varchar(20) primary key not null,
                            name text not null,
                            account varchar(256) not null,
                            password varchar(256) not null,
                            email_or_phone varchar(150),
                            note text);''')
        self.dbcon.commit()

    def sql_regexp_search(self, regexp, exp) -> bool:
        # sql正则表达式搜索
        return re.search(regexp, exp) is not None

    # 对外的槽函数
    def get_db_name(self, name):
        # 连接到数据库
        self.name = name
        self.dbcon = sql.connect(userDataDb)
        self.dbcon.create_function('regexp', 2, self.sql_regexp_search)
        self.dbcur = self.dbcon.cursor()
        self.isConnectToDB = True
        self.check_table_exists()

    def add_useritem(self, useritem: UserItem):
        # 插入一条useritem
        try:
            self.dbcur.execute('''insert into userdata
                                values (?, ?, ?, ?, ?, ?);
            ''', (useritem.id, useritem.name, useritem.account, useritem.password, useritem.email_or_phone, useritem.note))
            self.dbcon.commit()
            self.addItemSignal.emit(True, useritem)
        except sql.OperationalError as e:
            self.dbcon.rollback()
            self.addItemSignal.emit(False)
            print('add error: ', e)

    def delete_useritem(self, ID: str):
        try:
            # 删除对应id项目
            self.dbcur.execute('''delete from userdata
                                where id = ?;
            ''', (ID,))
            self.dbcon.commit()
            self.deleteItemSignal.emit(True, ID)
        except sql.OperationalError as e:
            self.dbcon.rollback()
            self.deleteItemSignal.emit(False, ID)
            print('delete error: ', e)

    def load_items(self):
        try:
            self.dbcur.execute('select * from userdata;')
            self.dbcon.commit()
            buff = self.dbcur.fetchall()
            # 将列表转换成字典
            itemList = {}
            for item in buff:
                itemList[item[0]] = UserItem(item[0], item[1], item[2], password=item[3], email_or_phone=item[4], note=item[5])
            self.sendUserItemsSignal.emit(itemList)
        except sql.OperationalError as e:
            print('load error: ', e)

    def modify_useritem(self, ID: str, item: str, value: str):
        try:
            self.dbcur.execute('''update userdata
                                set {}=? where id = ?;
            '''.format(item), (value, ID))
            self.dbcon.commit()
            self.modifySignal.emit(True, ID, item, value)
        except sql.OperationalError as e:
            self.dbcon.rollback()
            self.modifySignal.emit(False, ID, item, value)
            print('modify error: ', e)

    def get_new_name(self, name: str):
        self.newName = name

    def filite_useritem(self, item: str, descript: str):
        try:
            if self.setting.useRegExpFilite is True:
                # 使用正则表达式搜索
                if item == '*':
                    self.dbcur.execute('''select id from userdata
                                        where name regexp '{}' or account regexp '{}' or email_or_phone regexp '{}';
                    '''.format(descript, descript, descript))
                else:
                    self.dbcur.execute('''select id from userdata
                                        where {} regexp '{}';
                    '''.format(item, descript))
            else:
                # 仅使用关键字搜索
                if item == '*':
                    self.dbcur.execute('''select id from userdata
                                        where name like '%{}%' or account like '%{}%' or email_or_phone like '%{}%';
                    '''.format(descript, descript, descript))
                else:
                    self.dbcur.execute('''select id from userdata
                                        where {} like '%{}%';
                    '''.format(item, descript))
            # 获取查询结果
            buff = self.dbcur.fetchall()
            buff = [b[0] for b in buff]
            self.filiteResSignal.emit(buff)
        except sql.OperationalError as e:
            print('filite error: ', e)

    def get_setting(self, setting: Setting):
        self.setting = setting
        # 需要自动备份，登陆后自动备份
        if self.setting.autoBackup is True and self.backupDatabaseFlag is False:
            self.backup_database()
            self.backupDatabaseFlag = True
