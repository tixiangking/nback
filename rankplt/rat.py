import matplotlib

matplotlib.use('Agg')

import numpy as np

import pandas as pd

#关于import这些玩意，请使用 sudo apt install python-XXX

import matplotlib.pyplot as plt

from matplotlib import mlab

from matplotlib import rcParams

data=[3,3,3,5,7,6,398,522,823,792,822,855]

rn=['10','20','30','50','80','130','1000','2000','3000','5000','8000','13000']

vbar1=[3,3,4,4,5,6,5,9,7,9,8,8]

#vbar2=[4,6,9,2,7,8,10,8,12,6]

fig, ax1 = plt.subplots(figsize=(20,15))

x=np.arange(len(rn))

y=np.array(list(vbar1))

#w=np.array(list(vbar2))
plt.xticks(fontsize=13)
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

ax2.plot(x,z,c='y',marker='o', linewidth=5)

#打印折线图的数据

for a,b in zip(x,z):
   plt.text(a, b, '%s' % b, ha='center', va= 'bottom',fontsize=10)

ax1.set_xlabel('numbers of bridges', color='c', fontsize=30)
ax1.set_ylabel('mean error before compensation(\u03bc s)', color='c', fontsize=30)
ax1.tick_params(axis='y', labelcolor='c', labelsize=30)
ax2.set_ylabel('mean error after compensation(ns)', color='y', fontsize=30)
ax2.tick_params(axis='y', labelcolor='y', labelsize=30)

plt.tight_layout()
#保存成图片

plt.savefig("reddit.png",format='png')

