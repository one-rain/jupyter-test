# 1、概述
my jupyter test


# 2、准备工作

## 2.1、安装Jupyter
先修改配置文件

`NotebookApp.allow_password_change=True`

`jupyter notebook password`


```Shell
# 生成配置文件
jupyter notebook --generate-config

# 修改配置文件
vim ~/.jupyter/jupyter_notebook_config.py

# 启动
jupyter-lab

# 

```


# 3、Python命名规范

|名称|规范|举例|
|---|---|---|
|文件|全小写，多个单词之间用下划线|ad_stats.py|
|包|应该是简短的、小写的名字，尽量避免使用下划线|mypackage|
|模块|与包的规范同|mymodule|
|类|总是使用首字母大写单词串|AdStats|
|普通函数|小写字母，单词之间用_分割|my_example_function|
|私有函数|以__开头（两个下划线），其他和普通变量一样|`__get_name()`|
|专有函数|以__开头，__结尾|`__init__`，`__main__`|
|普通变量|尽量小写, 如有多个单词，用下划线隔开|this_is_a_var|
|实例变量|以_开头，其他和普通变量一样|`_instance_var`|
|私有实例变量|以__开头（两个下划线），其他和普通变量一样|`__private_var`|
|专有变量|以__开头，__结尾，一般为python的自有变量|`__doc__`|
|全局变量|全大写，多个单词之间用下划线隔开|如：MAX_CLIENT|

