# wordcloud
为gocqhttp设计的简易词云插件

# 本地部署
+ 需要
  - Python3.6+
    * requests
    * websockets
    * jieba
    * wordcloud
    * 以上均为需要 pip install 的python包。

# 启动命令
[Windows] python main.py
[Linux] python3 main.py

# 编译方法
pyinstaller main.spec
**可能需要手动修改 wordcloud 的源码，方法请自行谷歌。**
编译后可以直接运行可执行文件，但是我打包不出来，大佬可以自己试试。

# 需要
+ [字体] simsun.ttf 直接存放在 main.py 同目录处。
