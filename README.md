# py-passwordmanager
A lite password manager

------

*   加密并保存密码
*   生成随机密码

### 与数据库通信

#### 响应规则

1.  **加载所有项目：**主界面主动发送加载请求，数据库收到后将数据表中所有数据组合成python字典，`key`为`UserItem`对象的`id`属性，`value`为`UserItem`对象
2.  **添加项目：**主界面弹出添加项目表单，点击确认添加后，在检查无误的情况下，主界面将添加信息组合成`UserItem`对象，发送到数据库，数据库将此对象存入后返回添加成功或者失败的信号；若添加成功，主界面将新建项目添加到`tableWidget`中
3.  **删除项目：**与规则2基本相同
4.  **筛选项目：**主界面筛选框光标有变化时发送筛选信号，筛选信号参数为：*筛选范围*，分为“全部”、“名称”、“账号、“邮箱/电话”；*筛选条件*，默认使用关键字查找，也可以考虑一下支持正则表达式。数据库返回满足筛选条件的项的`ID`列表
5.  **修改项目：**主界面`tableWidget`中项被修改时发送，参数为被修改项的`ID`、被修改项的属性、被修改项的值，数据库进行更新，无需反馈信号

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

### 创建用户

第一次启动，弹出创建用户窗口；只允许单个用户，只需要密码进入，生成`密码 + timestamp`的`md5`保存在数据库中用于验证。

### 管理员密码要求

*   长度为`6~256`
*   允许包含大小写字母、数字及特殊字符（`+ - * / . @`）

### 进入密码管理器

输入的密码进行`md5`运算得到密钥，用数据库或注册表中保存的密钥验证，若成功则进入；否则在$n$ 次失败后锁定（或者删库）

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210124232544336.png" alt="image-20210124232544336" style="zoom:70%;" />

### 管理密码

添加密码，弹出一个表单填写，列举出如下项目

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210125145519105.png" alt="image-20210125145519105" style="zoom:80%;" />

每一个项目都有一个独立id作为标识，id为添加时刻时间戳，不在表中显示

|  ID  | 命名   | 账号      | 密码       | 手机/邮箱        | 备注   |
| :--: | ------ | --------- | ---------- | ---------------- | ------ |
| `id` | `name` | `account` | `password` | `email_or_phone` | `note` |

其中，`名称`，`账号`，`密码`为必填项，`密码`需要加密保存，加密时使用管理员密码（也就是用户进入时输入的密码）的`hash`（跟上面不一样）

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210125003050172.png" alt="image-20210125003621392" style="zoom:80%;" />

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210125003721871.png" alt="image-20210125003721871" style="zoom:80%;" />

*   单击表头按表头内容自动排序
*   搜索框根据表头按照关键字筛选，实时显示
*   `名称`，`账号`，`邮箱/电话`在双击单元格后可编辑
*   密码默认显示`******`，不可编辑，点击`查看`之后显示可编辑
*   操作栏为`删除`按钮，点击后弹出验证窗口，输入密码后（`hash + salt`验证）及确认后，该项目被删除
*   点击`添加`按键弹出对话框，完善对话框中选项后确认添加新项目

### 自动上锁

$n$ 分钟内无操作，密码管理器锁定，需要重新登录

### 密码生成

附加功能

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210125144115358.png" alt="image-20210125144115358" style="zoom:80%;" />



