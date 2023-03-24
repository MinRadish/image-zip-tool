# python-tool

- 图片压缩体积|尺寸



## 打包方式（**pyinstaller**）

1.  安装

    ~~~shell
    pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
    ~~~

2.  打包

    ~~~shell
    # Win
    pyinstaller -F -w -i xxx.ico ***.py
    # MAC[待测试]
    pyinstaller -w --clean -p 依赖包路径 入口文件.py
    
    -F参数表示覆盖打包，这样在打包时，不管我们打包几次，都是最新的，固定命令。-w表示窗体程序,--icon是设置exe的显示图标，'main.py'是程序的入口（如果是单个文件就换成文件名，如：hello.py），--noconsole 表示不展示cmd窗口，反过来想看cmd窗口就改成--console。*.ico文件可以到网上ico矢量图在线转换工具处理。
    ~~~

    

