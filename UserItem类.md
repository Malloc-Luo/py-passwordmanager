### `UserItem`类

#### 初始化

```python
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
        # 密码明文，使用后删除
        self._plainpswd = _plainpswd
        
        if not ((self.password is None) ^ (self._plainpswd is None)):
            raise ValueError('密文和明文在初始化时有且仅有一个为有效') 
```

需要注意的是，在`UserItem`对象构造时，需要保证`password`和`_plainpswd`由且仅有一个为`None`

如果初始化时为`_plainpswd`赋值，需要在后续调用`load_key(self, key)`加密

#### 索引

`UserItem`类重载了`__setitem__`和`__getitem__`方法，使用关键字或者序号索引赋值

|          属性          |       关键字索引       | 序号索引 |
| :--------------------: | :--------------------: | :------: |
|        `uI.id`         |       `uI['id']`       | `uI[0]`  |
|       `uI.name`        |      `uI['name']`      | `uI[1]`  |
|      `uI.account`      |    `uI['account']`     | `uI[2]`  |
|     `uI.passowrd`      |    `uI['passowrd']`    | `uI[3]`  |
| `uI.email_or_password` | `uI['email_or_phone']` | `uI[4]`  |
|       `uI.note`        |      `uI['note']`      | `uI[5]`  |

### 与数据库通信：

#### 响应规则

1.  **加载所有项目**：主界面主动发送加载请求，数据库收到后将数据表中所有数据组合成python字典，`key`为`UserItem`对象的`id`属性，`value`为`UserItem`对象
2.  **添加项目**：主界面弹出添加项目表单，点击确认添加后，在检查无误的情况下，主界面将添加信息组合成`UserItem`对象，发送到数据库，数据库将此对象存入后返回添加成功或者失败的信号；若添加成功，主界面将新建项目添加到`tableWidget`中
3.  **删除项目**：与规则2基本相同
4.  **筛选项目**：主界面筛选框光标有变化时发送筛选信号，筛选信号参数为：*筛选范围*，分为“全部”、“名称”、“账号、“邮箱/电话”；*筛选条件*，默认使用关键字查找，也可以考虑一下支持正则表达式。数据库返回满足筛选条件的项的`ID`列表
5.  **修改项目**：主界面`tableWidget`中项被修改时发送，参数为被修改项的`ID`、被修改项的属性、被修改项的值，数据库进行更新，无需反馈信号

#### 主界面向数据库发送

在数据库端需要实现的槽函数：

1.  `def delete_useritem(ID:str)`：主界面向数据库发送删除信号，参数为该项的`ID`，在数据库中删除该`ID`对应项，删除后回应删除成功或者失败信号
2.  `def filite_useritem(item:str, descript:str)`：主界面向数据库发送筛选信号，`item`为对应筛选项，如果是`*`就是所有项；`descript`是筛选条件；筛选后数据库发送满足条件项的`ID`列表
3.  `def add_useritem(useritem:UserItem)`：`useritem`为`UserItem`对象，添加后向主界面发送成功或者失败信号
4.  `def load_items()`：主界面向数据库发送加载信号，收到信号后数据库加载所有项，并向主界面发送`value`为`UserItem`对象、`key`为`UserItem.id`的字典
5.  `def modify_useritem(ID:str, item:str, value:str)`：主界面向数据库发送修改信号，`ID`是修改项的`id`，`item`是修改的属性，`value`为修改的值，数据库无需回应

#### 数据库向主界面发送

在主界面需要实现的槽函数：

1.  `def get_delete_res(issucce:bool)`：删除项目结果，若为`True`则成功删除
2.  `def get_filite(luserItemId:list)`：筛选的结果，`luserItemId`为满足筛选条件的项`ID`
3.  `def get_add_res(issucce:bool)`：添加项目结果，若为`True`则成功删除
4.  `def load_items(duserItem:dict)`：`duserItem`为`UserItem`字典，由数据库发送