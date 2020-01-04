# PKUPC-Code-Archiver

*便捷地存档您在北京大学计算概论A编程网格上提交的代码！*

### 创作缘由

`PKUPC-Code-Archiver`主要是我在maintain[Key-to-PKUPC](https://github.com/wr786/Key-to-PKUPC)时觉得每次都要复制我在编程网格上提交的代码再存到新建的`.cpp`文件里，单个的题也就算了，但是对于一整份作业题集，一个一个地去打开每个题目，点击提交历史，找到“我的”，然后打开最上面的“Passed”记录，实在是太烦了！

于是我便为了它写了个爬虫。

**从此再也不用担心助教在作业中再放重复的习题！**

### 使用方法

0. `pip install -r requirements.txt`

1. 启动目录下的`HAJIMERU.bat`，随后可能会跳出一个Chrome窗口，最小化即可，不用理睬。

2. 在看到`请输入您想要archive的题集的url:`这句话后，复制粘贴您想要archive的题集的url。

   比如，如果我想archive`lxz`班的`第八次作业--函数与递归（1）`，那么我只需打开这个题集，并且复制地址栏中的`http://162.105.86.10/programming/course/f6560de763094fc6b6e67cf385f45564/showProblemList.do?problemsId=9ae1dfceb663496aa623a2f48e5262d3`并粘贴，敲下回车即可。

3. 看到相应的提示时输入您的用户名和密码并敲下回车（放心，`PKUPC-Code-Archiver`没有采集您用户名和密码的功能）。

4. 喝一口水，看到`Chrome`窗口在任务栏的图标消失之后，回到目录下的`output`文件夹中收获您的`.cpp`源码文件！

### 可能遇到的问题

1. `PKUPC-Code-Archiver`需要您先安装好`Python3`和`Google Chrome`。

2. 报错与`chromedriver`相关：如果错误信息提示的是“和Chrome版本不一致”的意思，请自行将`chromedriver`和Chrome更新成同一个版本。