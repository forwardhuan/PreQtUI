# 简介
一款为了预览PyQt5设计的UI界面而开发的工具，使用时需要结合PyCharm同时使用。

![在这里插入图片描述](https://img-blog.csdnimg.cn/023500ddf5fa4eada7aebc3dc944961f.png)

# 下载
[PyQt5界面预览工具](https://gitee.com/tool_huan/pre-qt-ui/releases)

# 参数说明
![在这里插入图片描述](https://img-blog.csdnimg.cn/4cbc83c40266473e96e8ddc6117cb0c5.png)

# 使用配置
1. 启动PyCharm，找到`File -> Settings`，打开
![在这里插入图片描述](https://img-blog.csdnimg.cn/c2d9703b03a9469884f5237ee5f36d57.png)
2. 找到`Tools -> External Tools`点击打开，在新界面中点击添加按钮
![在这里插入图片描述](https://img-blog.csdnimg.cn/19a222cda03149cca303c6aaf83db476.png)
3. 添加新的扩展工具，配置如下，配置完成后点击OK
![在这里插入图片描述](https://img-blog.csdnimg.cn/22953bf30cb14c83a9d08cea4f0db24d.png)
	- `Name` 扩展工具的显示名称
	- `Program` PreQtUI所在路径
	- `Argument` 运行时参数设置 `-f $FilePath$ -r $ProjectFileDir$`
	- `Working directory` 工作路径 `$ProjectFileDir$`

4. 点击`Apply`, 再点击`OK`确认
![在这里插入图片描述](https://img-blog.csdnimg.cn/9b1a200ac74f42c7a96c0ae0fe24b72b.png)
5. 此时配置已完成，打开一个PyQt5开发的项目实验一下。鼠标右键一个使用QtDesigner设计转换成的UI python文件，会发现在`External Tools`下有一个刚配置的`PreQtUI`选项，点击可以预览该界面文件的UI布局。
![在这里插入图片描述](https://img-blog.csdnimg.cn/57fb3bb5fcaa4e4e95f036dc5c2896e6.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/f6471db1aeec4b56a0831ced7cdb863f.png)
6. 关闭预览窗口，可以看到下面的`PreQtUI`窗口输出本次运行日志，同时会在项目根目录生成一个可执行的`PreQtUI.py`文件。简单修改其内容可以直接运行设计的UI界面。
![在这里插入图片描述](https://img-blog.csdnimg.cn/53dfa547d5ff4599805f199595a84850.png)

7. 如果感觉`PyQtUI`的层级太深，可以按照以下设置重新设置`PyQtUI`的位置。打开`File -> Settings -> Menus and Tools -> Project View Popup Menu`
![在这里插入图片描述](https://img-blog.csdnimg.cn/d7636e2664da419aa8b5883075ad15aa.png)
8. 选择一个想添加的位置，点击上方`+`号，选择`Add Action`
![在这里插入图片描述](https://img-blog.csdnimg.cn/9117af8919b54c85b1c7deb7ad3f1eef.png)
9. 找到`External Tools`，向下点击找到添加的扩展工具`PreQtUI`并选中
![在这里插入图片描述](https://img-blog.csdnimg.cn/049697f3d629487bb004fbc6ed2dd2e3.png)
 10. 此时，`PreQtUI`就被添加上了，同时也可下在下方添加分割线，通过上下按钮移动其显示位置。
![在这里插入图片描述](https://img-blog.csdnimg.cn/adf46a0ce42f443a948a151fcc9904ff.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d5134a7bca0f4781b5f64154b3aef713.png)
10. 点解`OK`， 重新执行，可以看到`PreQtUI`出现在了最外层
![在这里插入图片描述](https://img-blog.csdnimg.cn/74d2e618db484989866c9801313b87fb.png)
