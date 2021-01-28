# -*- coding:utf-8 -*-
import sys, os
from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3 as sql
from UserItem import UserItem
from Common import dbAbsPath


class DataBase(QObject):
    # 发送UserItem对象的字典
    sendUserItemsSignal = pyqtSignal(dict)
    # 筛选结果信号
    filiteResSignal = pyqtSignal(str)
    # 删除结果的信号
    deleteItemSignal = pyqtSignal(bool, str)
    # 添加结果的信号
    addItemSignal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.dbcon = None
        self.dbcur = None
        # 是否连接到了数据库
        self.isConnectToDB = False
        self.newName = ''
        self.name = ''
        self.get_db_name('')

    def __del__(self):
        if self.isConnectToDB == True:
            self.dbcur.close()
            self.dbcon.commit()
            self.dbcon.close()
            # os.rename(self.name, self.newName)

    def check_table_exists(self):
        """ 检查数据表data.db是否存在   
        """
        # 检查数据表是否存在，不存在则创建一个
        self.dbcur.execute('''create table if not exists 
                              userdata(id varchar(20) primary key not null,
                                        name text not null,
                                        acount varchar(256) not null,
                                        password varchar(256) not null,
                                        email_or_phone varchar(150),
                                        note text);
        ''')
        self.dbcon.commit()


    # 对外的槽函数
    def get_db_name(self, name):
        # 连接到数据库
        self.name = name
        self.dbcon = sql.connect(dbAbsPath + 'data.db')
        self.dbcur = self.dbcon.cursor()
        self.isConnectToDB = True
        self.check_table_exists()

    def add_useritem(self, useritem:UserItem):
        print('ADD', useritem)
        # 插入一条useritem
        try:
            self.dbcur.execute('''
            insert into userdata
            values (?, ?, ?, ?, ?, ?);
            ''', (useritem.id, useritem.name, useritem.account, useritem.password, useritem.email_or_phone, useritem.note))
            self.dbcon.commit()
            self.addItemSignal.emit(True)
        except:
            self.addItemSignal.emit(False)
            print('add error')

    def delete_useritem(self, ID:str):
        try:
            # 删除对应id项目
            self.dbcur.execute('''
            delete from userdata
            where id = ?;
            ''', (ID,))
            self.dbcon.commit()
            self.deleteItemSignal.emit(True, ID)
        except:
            self.deleteItemSignal.emit(False, ID)
            print('delete error')

    def load_items(self):
        print('load')
        try:
            self.dbcur.execute('''
            select * from userdata;
            ''')
            self.dbcon.commit()
            buff = self.dbcur.fetchall()
            print(buff)
            # 将列表转换成字典
            itemList = {}
            for item in buff:
                itemList[item[0]] = UserItem(item[0], item[1], item[2], item[3], item[4], item[5])
            self.sendUserItemsSignal.emit(itemList)
        except:
            print('load error')

    def modify_useritem(self, ID:str, item:str, value:str):
        try:
            self.dbcur.execute('''
            update userdata
            set {}=?
            where id = ?;
            '''.format(item), (value, ID))
            self.dbcon.commit()
        except:
        # 报错
            print('modify error')

    def get_new_name(self, name:str):
        self.newName = name
