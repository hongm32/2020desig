# 公交线路客流量图

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# 指定默认字体，负号显示问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel("27路和49路公交线路客流量表.xlsx", header=1)
plt.figure(figsize=(12, 12))  # 自定义画布大小，单位英寸
plt.plot(df['时间段'], df['27路'], linewidth='1', label="小明乘坐线路(27路)", marker='o')
plt.plot(df['时间段'], df['49路'], linewidth='1', label="妈妈乘坐线路(49路)", marker='o', markersize=6)
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('公交线路客流量', size=20)  # 图表标题
plt.xlabel("时间段", size=12)  # 横轴标题
plt.ylabel("客流量", size=12)  # 纵轴标题
plt.gca().spines["right"].set_color("none")  # right边框属性设置为none不显示
plt.gca().spines["top"].set_color("none")  # top边框属性设置为none不显示
plt.show()  # 显示
