#加载包
import numpy as np #常用数学函数库
import matplotlib.pyplot as plt #常用绘图库
from mpl_toolkits.mplot3d import Axes3D #3D绘图库

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#加载数据
data = np.genfromtxt('C:/Users/Administrator/Desktop/test.csv',
                     delimiter=',',skip_header=1)#根据文件具体信息更改
X = data[:,:3]#切片取第0列，第1列，第2列
Y = data[:,4]#切片取第4列

#绘制3D散点图
ax = Axes3D(plt.figure(),azim=65,elev=15)#azim,elev设置角度
fig = ax.scatter(X[:, 0], X[:, 1], X[:, 2],
           s=20, c=Y, cmap=plt.get_cmap('brg'),
           depthshade = False)#s=size,c=color,cmap可选各种图,depthshade默认渲染

#设置标题
ax.set_title("3D-Scatter")

#设置轴标签
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

#设置轴上下限
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

#设置图例
cb = plt.colorbar(fig,fraction=0.15,shrink=0.5,pad=0.01)
cb.set_ticks(np.arange(1,4))
cb.set_ticklabels(['a','b','c'])

plt.show()
