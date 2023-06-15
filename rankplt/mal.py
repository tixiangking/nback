import matplotlib

matplotlib.use('Agg')

import numpy as np

import pandas as pd

#关于import这些玩意，请使用 sudo apt install python-XXX

import matplotlib.pyplot as plt

from matplotlib import mlab

from matplotlib import rcParams

data=[9.39,8.93,9.4,9.06,9.61,9.74,9.3,9.38,9.22,9.75,9.34,9.58]

rn=['12','13','14','15','16','17','18','19','20','21','22','23']

vbar1=[1109,851,881,591,1279,1166,700,669,702,1707,1653,1341]

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

plt.savefig("mal.png",format='png')


