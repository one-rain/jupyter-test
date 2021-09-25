import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
root_path = current_directory[:current_directory.find("jupyter-test")+len("jupyter-test")]
print(root_path)

data_path = os.path.abspath(root_path + os.path.sep + 'data' + os.path.sep + 'mingri' + os.path.sep + '5-5_tiwen.xls')
print(data_path)

plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df = pd.read_excel(data_path)

#折线图
x = df['日期']                  #x轴数据
y = df['体温']                  #y轴数据
plt.plot(x,y,color='m',linestyle='-',marker='o',mfc='w')
plt.xlabel('2020年2月')        #x轴标题
plt.ylabel('基础体温')         #y轴标题

#设置x轴刻度及标签
dates = ['1日','2日','3日','4日','5日',
            '6日','7日','8日','9日','10日',
            '11日','12日','13日','14日']

plt.xticks(range(1,15,1), dates)

#坐标轴范围
#plt.xlim(1, 14)
#plt.ylim(35, 45)
#plt.show()

plt.yticks([35.4,35.6,35.8,36,36.2,36.4,36.6,36.8,
            37,37.2,37.4,37.6,37.8,38])
for a,b in zip(x,y):
    plt.text(a,b+0.05,'%.1f'%b,ha = 'center',va = 'bottom',fontsize=9)
#图例
plt.legend()
#绘制一个两端缩进的箭头
plt.annotate('最高体温', xy=(9,37.1), xytext=(10.5,37.1),
            xycoords='data',
            arrowprops=dict(facecolor='r', shrink=0.05))
plt.show()

