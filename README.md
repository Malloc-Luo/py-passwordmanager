# py-passwordmanager
A lite password manager

------

*   加密并保存密码
*   生成随机密码

### 创建用户

第一次启动，弹出创建用户窗口；只允许单个用户，只需要密码进入，生成密码的`hash + salt`保存在数据库或者注册表中用于验证。

### 管理员密码要求

*   长度为`6~256`
*   允许包含大小写字母、数字及特殊字符（`+ - * / . @`）

### 进入密码管理器

输入的密码进行`hash + salt`运算得到密钥，用数据库或注册表中保存的密钥验证，若成功则进入；否则在$n$ 次失败后锁定（或者删库）

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



