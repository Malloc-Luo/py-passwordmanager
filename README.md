# py-passwordmanager
A lite password manager

------

### UPDATE LOG

#### 0.11.2

*   添加帮助文档，使用说明

#### 0.11.1

*   修复一些小问题

#### 0.11.0

*   适配linux平台，仅目前测试过ubuntu 20.04
*   修复一些小问题

#### 0.10.7

*   调整部分ui

#### 0.10.6

*   增加一些Messagebox样式

#### 0.10.5

*   增加一些设置项

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
*   提升安全性，实现全部加密
*   增加数据库导入功能

### BUGS

*   ~~3分钟无响应自动锁定有时失效~~
*   文件加密机制问题
*   ~~主界面的子界面关闭逻辑~~
*   ~~自动备份文件~~

### 创建用户：

第一次启动，弹出创建用户窗口；只允许单个用户，只需要密码进入，生成`密码 + timestamp`的`md5`保存在数据库中用于验证。

### 管理员密码要求：

*   长度为`6~256`
*   允许包含大小写字母、数字及特殊字符（`+ - * / . @`）

### 进入密码管理器：

输入的密码进行`md5`运算得到密钥，用数据库或注册表中保存的密钥验证，若成功则进入；~~否则在$n$ 次失败后锁定（或者删库）~~

<img src="readme\image-20210129013101290.png" alt="image-20210207162816195" style="zoom:80%;" />

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

