### 基本功能



#### 一、添加密码项目

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210220114447693.png" alt="image-20210220114447693" style="zoom:80%;" />

点击右侧第一个按钮，填出表单，填写完成表单后点击“保存”即可。其中“名称”、“账号”、“密码”为必填项，缺省可以使用“_”代替。”密码“项可以选择自动生成随机密码，更安全。

#### 二、删除项目

选中表中行，点击右侧第二个按钮，或者点击鼠标右键，选择”删除“即可删除行。注意，当前版本删除后无法直接恢复。

#### 三、设置

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210220115158511.png" alt="image-20210220115158511" style="zoom:80%;" />

以上为当前可选设置项目。

1.  **无动作自动锁定时间(分)**：密码管理器打开后，用户在一段时间没有操作密码管理器，软件会自动锁定，需要重新输入密码进入
2.  **显示tooltips**：若显示tooltips则在鼠标悬停在单元格上时会显示内容提示气泡。
3.  **显示行号**：显示行号
4.  **删除时确认提示**：是否显示删除项目时的确认弹窗。
5.  **使用正则表达式搜索**：使用左上角筛选框筛选查找项目时使用[正则表达式](https://deerchao.cn/tutorials/regex/regex.htm)，筛选更加高效
6.  **自动备份**：登录时自动备份当前数据文件
7.  **按住Ctrl显示密码**：默认选中行后自动显示密码，选择该项后需要按住Ctrl键（Linux系统上为按住Alt键）才能显示密码。
8.  **鼠标单击选中行**：默认鼠标单击选中行，取消该项后为鼠标悬停时选中行。

#### 四、编辑修改

选中单元格后双击，即可进行编辑。

#### 五、更新

在”关于“界面点击右下角”检查更新“项，若有更新可用，则会自动跳转打开软件[release网站](https://github.com/Malloc-Luo/py-passwordmanager/releases/tag/0.11.1)，目前需要手动下载，覆盖更新。

<img src="D:%5CFileBox%5CCode%5CPython%5CPasswordManager%5Cpy-passwordmanager%5Creadme%5Cimage-20210220121012345.png" alt="image-20210220121012345" style="zoom:80%;" />



### 常见问题

1.  如何修改登录密码：当前版本尚不支持修改登录密码；
2.  如何迁移数据：当前版本尚不支持迁移数据（其实也可以）；
3.  如何使用备份文件：数据文件储存目录默认为：windows下：`C:\Users\[user]\AppData\Local\py-passwordmanager`，备份文件在其下`backup\`，如若需要使用备份文件，找到任意版本备份文件，重命名为`data.db`，替换掉原有`data.db`即可。