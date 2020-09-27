import numpy as np
import pandas as pd

click_series = pd.read_csv("D:/wangrun/data/theme_click_log.csv")
#click_series = pd.read_csv("D:/wangrun/data/theme_click_log.csv", sep = ",", header = 0)
click_series.head()    # 查看前几行（默认5行）
click_series.tail(10)
click_series.shape     # 查看数据的形状，返回（行数、列数）
click_series.columns   # 查看列名列表
click_series.index     # 查看索引列
click_series.dtypes    # 查看每一列的数据类型

