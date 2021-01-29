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

