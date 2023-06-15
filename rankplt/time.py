import matplotlib

matplotlib.use('Agg')

import numpy as np

import pandas as pd

#关于import这些玩意，请使用 sudo apt install python-XXX

import matplotlib.pyplot as plt

from matplotlib import mlab

from matplotlib import rcParams

data=[9.28,8.95,9.44,9.1,9.58,9.68,9.41,9.19,9.21,9.79]

rn=['1','2','5','8','15','0.6','0.7','0.8','0.9','1']

vbar1=[8201,6701,7178,6344,7448,8167,6442,6116,6923,10825]

#vbar2=[4,6,9,2,7,8,10,8,12,6]

fig, ax1 = plt.subplots(figsize=(15,10))

x=np.arange(len(rn))

y=np.array(list(vbar1))

#w=np.array(list(vbar2))

xticks1=list(rn)

#条形图

#plt.bar(x[0:6],y[0:6],width = 0.45,align='center',color = 'gray',alpha=0.9)

#plt.bar(x[6:],y[6:],width = 0.45,align='center',color = 'c',alpha=0.9)

#上面这两条语句，是用来设置条形图的颜色的，前6条柱子是gray色，而后四条是蓝绿色

plt.bar(x,y,width = 0.45,label='female',align='center',color = 'c',alpha=0.9)

#plt.bar(x,w,bottom=vbar1,label='male',tick_label=vbar1,width = 0.45,align='center',color = 'y',alpha=0.9)

#看我斜体数据，就是关键了

plt.xticks(x,xticks1,size='medium')


for a,b in zip(x,y):
    plt.text(a,b,'%s' %b,ha='center',va='top',fontsize=10)

#折线图

ax2 = ax1.twinx()

z=np.array(list(data))

ax2.plot(x,z,c='y',marker='o')

#打印折线图的数据

for a,b in zip(x,z):
   plt.text(a, b, '%s' % b, ha='center', va= 'bottom',fontsize=10)

plt.tight_layout()
#保存成图片

plt.savefig("time.png",format='png')


