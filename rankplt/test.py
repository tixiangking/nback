import codecs
import numpy as np
pt_be=0
pt_up=0
bor=82
f1 = codecs.open('w1.txt', mode='r', encoding='utf-8')
f2 = codecs.open('w2.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line1 = f1.readline()   # 以行的形式进行读取文件
list1 = []
while line1:
    a = line1.split()
    b = a[2:3]   # 这是选取需要读取的位数
    list1.append(b)  # 将其添加在列表之中
    data1=np.array(list1)
    line1 = f1.readline()
f1.close()
data1=data1[:,0]
data1=list(map(float, data1))
line2 = f2.readline()   # 以行的形式进行读取文件
list2 = []
while line2:
    a = line2.split()
    b = a[2:3]   # 这是选取需要读取的位数
    list2.append(b)  # 将其添加在列表之中
    data2=np.array(list2)
    line2 = f2.readline()
f2.close()
data2=data2[:,0]
data2=list(map(float, data2))
#x= data[0]+1
#print(data1)
#print(data2)
leng=len(data1)
data_be=data1[0:bor]+data2[0:bor]
data_up=data1[(bor+1):leng]+data2[(bor+1):leng]
for i in range(bor):
    if data_be[i]>25.0:
        pt_be=pt_be+data_be[i]
for i in range(bor+1,leng):
    if data_up[i]>25.0:
        pt_up=pt_up+data_up[i]
pt=pt_up*0.4421+pt_be*0.68
print(pt)
