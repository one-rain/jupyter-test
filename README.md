# jupyter-test
my jupyter test


### 设置密码

先修改配置文件

`NotebookApp.allow_password_change=True`

`jupyter notebook password`


```Shell
# 生成配置文件
jupyter notebook --generate-config

# 修改配置文件
vim ~/.jupyter/jupyter_notebook_config.py

# 启动
jupyter notebook

# 

```

> 参考
> ![CentOS7安装jupyter](https://blog.csdn.net/iFan138/article/details/88424753)
