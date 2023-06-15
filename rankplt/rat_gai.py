import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import matplotlib
import numpy as np

matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

data = [3,3,3,5,7,6,398,522,823,792,822,855]
rn = ['10','20','30','50','80','130','1000','2000','3000','5000','8000','13000']
vbar1 = [3,3,4,4,5,6,5,9,7,9,8,8]

fig, ax1 = plt.subplots(figsize=(20,15))

x = np.arange(len(rn))
y = np.array(list(vbar1))

xticks1 = list(rn)

# Bar chart
ax1.bar(x, y, width=0.45, label='补偿前的平均同步误差', align='center', color='steelblue', alpha=0.9)

plt.xticks(x, xticks1, fontsize=20)

for a, b in zip(x, y):
    plt.text(a, b, '%s' % b, ha='center', va='bottom', fontsize=10, color='black')

# Line chart
ax2 = ax1.twinx()
z = np.array(list(data))
ax2.plot(x, z, label='补偿后的平均同步误差', c='darkorange', marker='o', linewidth=3)

for a, b in zip(x, z):
    plt.text(a, b, '%s' % b, ha='center', va='top', fontsize=10, color='black')

# Set labels
ax1.set_xlabel('网桥数量', color='black', fontsize=30)
ax1.set_ylabel('补偿前的平均同步误差(\u03bcs)', color='steelblue', fontsize=30)
ax2.set_ylabel('补偿后的平均同步误差(ns)', color='darkorange', fontsize=30)

# Change tick colors to match charts
ax1.tick_params(axis='y', labelcolor='steelblue', labelsize=20)
ax2.tick_params(axis='y', labelcolor='darkorange', labelsize=20)

# Add legends
ax1.legend(loc='upper left', fontsize=15)
ax2.legend(loc='upper right', fontsize=15)

plt.tight_layout()

# Save as image
plt.savefig("reddit_ch.png", format='png')
