# py-passwordmanager
A lite password manager

------

### UPDATE LOG

#### 0.10.4

*   改用自定义MessageBox，比自带的好看

#### 0.10.3

*   修复数据备份的bug

#### 0.10.2

*   修复about界面的几个小bug

#### 0.10.1

*   调整qrc文件，体积减小了80%，不知道是否有用

#### 0.10.0

比较大的更新，加了许多新功能
*   主界面UI调整，tabBar隐藏
*   添加自定义设置功能，目前自定义选项有限
*   添加'关于'界面，可以访问网站

#### 0.9.7

*   修复密码生成的一个小bug
*   密码生成后自动复制到粘贴板

#### 0.9.6

*   将密码生成界面移动到添加界面上，并完善该功能
*   移除之前的密码生成tabWidget界面

#### 0.9.5

*   优化右键菜单界面显示

#### 0.9.4

*   新增了操作提示气泡
*   新增主界面单元格tool tips

#### 0.9.3

*   修复了排序后tableWidget刷新内容混乱问题

#### 0.9.1

*   支持正则表达式搜索

#### 0.9.0

*   添加查询筛选功能，目前仅支持关键字查找
*   改掉一个数据库端的bug

#### 0.8.2

*   添加右键菜单
*   美化登录界面

### TO-DO:

*   ~~内容筛选~~
*   ~~用户自定义设置选项~~
*   ~~自定义MessageBox~~
*   ~~美化右键菜单~~
*   ~~正则表达式筛选~~
*   记录修改日志，可以回退修改、删除、添加等

### BUGS

*   ~~3分钟无响应自动锁定有时失效~~
*   文件加密机制问题
*   ~~主界面的子界面关闭逻辑~~
*   ~~自动备份文件~~

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

### 创建用户：

第一次启动，弹出创建用户窗口；只允许单个用户，只需要密码进入，生成`密码 + timestamp`的`md5`保存在数据库中用于验证。

### 管理员密码要求：

*   长度为`6~256`
*   允许包含大小写字母、数字及特殊字符（`+ - * / . @`）

### 进入密码管理器：

输入的密码进行`md5`运算得到密钥，用数据库或注册表中保存的密钥验证，若成功则进入；~~否则在$n$ 次失败后锁定（或者删库）~~

<img src="readme\image-20210129013101290.png" alt="image-20210131170058836" style="zoom:80%;" />

### 管理密码

添加密码，弹出一个表单填写，列举出如下项目

<img src="readme\image-20210129013231793.png" alt="image-20210131165433224" style="zoom:80%;" />

每一个项目都有一个独立id作为标识，id为添加时刻时间戳，不在表中显示

|  ID  | 命名   | 账号      | 密码       | 手机/邮箱        | 备注   |
| :--: | ------ | --------- | ---------- | ---------------- | ------ |
| `id` | `name` | `account` | `password` | `email_or_phone` | `note` |

其中，`名称`，`账号`，`密码`为必填项，`密码`需要加密保存，加密时使用管理员密码（也就是用户进入时输入的密码）的`hash`（跟上面不一样）

<img src="readme\image-20210129013402419.png" alt="image-20210131165807753" style="zoom:80%;" />

<img src="readme\image-20210129013436890.png" alt="image-20210131165944414" style="zoom:80%;" />

*   单击表头按表头内容自动排序
*   搜索框根据表头按照关键字筛选，实时显示
*   `名称`，`账号`，`邮箱/电话`在双击单元格后可编辑
*   密码默认显示`******`，不可编辑，点击`查看`之后显示可编辑
*   操作栏为`删除`按钮，点击后弹出验证窗口，输入密码后（`hash + salt`验证）及确认后，该项目被删除
*   点击`添加`按键弹出对话框，完善对话框中选项后确认添加新项目

### 自动上锁

$n$ 分钟内无操作，密码管理器锁定，需要重新登录

### 密码生成

附加功能，在添加密码页面进入，生成密码后，点击确定，生成的密码会自动填充到添加密码界面的密码框中

<img src="readme\image-20210131165245145.png" alt="image-20210131165245145" style="zoom:80%;" />

