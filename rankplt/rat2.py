import matplotlib

matplotlib.use('Agg')

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib import mlab

from matplotlib import rcParams

data=[3,3,3,5,7,6,398,522,823,792,822,855]

rn=['10','20','30','50','80','130','1000','2000','3000','5000','8000','13000']

vbar1=[3,3,4,4,5,6,5,9,7,9,8,8]

vbar2=[4,6,9,2,7,8,10,8,12,6]

fig, ax1 = plt.subplots(figsize=(20,10))

x=np.arange(len(rn))

y=np.array(list(vbar1))

w=np.array(list(vbar2))

xticks1=list(rn)

plt.bar(x,y,width = 0.45,label='female',align='center',color = 'tab:blue',alpha=0.9)

plt.bar(x,w,bottom=vbar1,label='male',tick_label=vbar1,width = 0.45,align='center',color = 'tab:orange',alpha=0.9)

plt.xticks(x,xticks1,size=14)

plt.yticks(fontsize=14)

for a,b in zip(x,y):
plt.text(a,b,'%s' %b,ha='center',va='top',fontsize=10)

for a,b in zip(x,w+vbar1):
plt.text(a,b,'%s' %b,ha='center',va='top',fontsize=10)

ax1.set_ylabel("Count",fontsize=16)

ax1.tick_params(axis='y',labelsize=14)

ax2 = ax1.twinx()

z=np.array(list(data))

ax2.plot(x,z,c='tab:green',marker='o', linewidth=5)

for a,b in zip(x,z):
plt.text(a, b, '%s' % b, ha='center', va= 'bottom',fontsize=10)

ax2.set_ylabel("Timestamps",fontsize=16)

ax2.tick_params(axis='y',labelsize=14)

ax1.set_xlabel("Numbers of bridges",fontsize=16)

plt.tight_layout()

plt.savefig("reddit.png",format='png')