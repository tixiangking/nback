import codecs
import math
import numpy as np
pt=0
rate1 = 2.8
rate2 = 3
rate3 = 3.4-0.5
rate4 = 3.5-0.2
rate5 = 3.6-0.5
rate6 = 3.7
rate7 = 3.4
rate8 = 3.5
rate9 = 3.6
f1 = codecs.open('w1.txt', mode='r', encoding='utf-8')
f2 = codecs.open('w2.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line1 = f1.readline()   # 以行的形式进行读取文件
list1 = []
while line1:
    a = line1.split()
    b = a[8:9]   # 这是选取需要读取的位数
    list1.append(b)  # 将其添加在列表之中
    data1=np.array(list1)
    line1 = f1.readline()
f1.close()
data1=data1[:,0]
for i in range(len(data1)):
    data1[i] = data1[i].replace(',','')
data1=list(map(float, data1))
    
line2 = f2.readline()   # 以行的形式进行读取文件
list2 = []    
while line2:
    a = line2.split()
    b = a[8:9]   # 这是选取需要读取的位数
    list2.append(b)  # 将其添加在列表之中
    data2=np.array(list2)
    line2 = f2.readline()
f2.close()
data2=data2[:,0]
for i in range(len(data2)):
    data2[i] = data2[i].replace(',','')
data2=list(map(float, data2))

data=data1+data2

for i in range(89):
    if data[i] <= 20:
        data[i]=2400/(math.e**(math.log(data[i],rate1)))
    elif data[i]<= 50:
        data[i]=2400/(math.e**(math.log(data[i],rate2)))
    elif data[i]<= 100:
        data[i]=2400/(math.e**(math.log(data[i],rate7)))
    elif data[i]<= 300:
        data[i]=2400/(math.e**(math.log(data[i],rate8)))
    elif data[i]<= 500:
        data[i]=2400/(math.e**(math.log(data[i],rate9)))
    else:
        data[i]=2400/(math.e**(math.log(data[i],rate6)))
        
    if data[i]>=0:
        pt=pt+data[i]
'''
for i in range(124,len(data)):
    if data[i] <= 20:
        data[i]=2400/(math.e**(math.log(data[i],rate1)))
    elif data[i]<= 50:
        data[i]=2400/(math.e**(math.log(data[i],rate2)))
    elif data[i]<= 100:
        data[i]=2400/(math.e**(math.log(data[i],rate7)))
    elif data[i]<= 300:
        data[i]=2400/(math.e**(math.log(data[i],rate8)))
    elif data[i]<= 500:
        data[i]=2400/(math.e**(math.log(data[i],rate9)))
    else:
        data[i]=2400/(math.e**(math.log(data[i],rate6)))
        
    if data[i]>=20:
        pt=pt+data[i]
'''

for i in range(99,272):
    if data[i] <= 20:
        data[i]=2400/(math.e**(math.log(data[i],rate1)))
    elif data[i]<= 50:
        data[i]=2400/(math.e**(math.log(data[i],rate2)))
    elif data[i]<= 100:
        data[i]=2400/(math.e**(math.log(data[i],rate7)))
    elif data[i]<= 300:
        data[i]=2400/(math.e**(math.log(data[i],rate8)))
    elif data[i]<= 500:
        data[i]=2400/(math.e**(math.log(data[i],rate9)))
    else:
        data[i]=2400/(math.e**(math.log(data[i],rate6)))
        
    if data[i]>=20:
        pt=pt+data[i]

for i in range(282,len(data)):
    if data[i] <= 20:
        data[i]=2400/(math.e**(math.log(data[i],rate1)))
    elif data[i]<= 50:
        data[i]=2400/(math.e**(math.log(data[i],rate2)))
    elif data[i]<= 100:
        data[i]=2400/(math.e**(math.log(data[i],rate3)))
    elif data[i]<= 300:
        data[i]=2400/(math.e**(math.log(data[i],rate4)))
    elif data[i]<= 500:
        data[i]=2400/(math.e**(math.log(data[i],rate9)))
    else:
        data[i]=2400/(math.e**(math.log(data[i],rate6)))
        
    if data[i]>=20:
        pt=pt+data[i]

print(pt)