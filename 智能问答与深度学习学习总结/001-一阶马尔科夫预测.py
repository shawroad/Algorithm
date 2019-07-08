"""

@file   : 001-一阶马尔科夫预测.py

@author : xiaolu

@time   : 2019-07-08

"""
# 简单理解 p(xn| x1, x2, x3, ..., xn-1) = p(xn | xn-1) 当前状态只与前一个状态有关。
import numpy as np
import matplotlib.pyplot as plt


# 总共六种状态，如状态1向状态1转移的概率就是1
P = np.matrix([[1, 0, 0, 0, 0, 0],
               [1/4, 1/2, 0, 1/4, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [1/16, 1/4, 1/8, 1/4, 1/4, 1/16],
               [0, 0, 0, 1/4, 1/2, 1/4],
               [0, 0, 0, 0, 0, 1]])

v = np.matrix([[0, 0, 1, 0, 0, 0]])   # 初试状态给定为3

plot_data = []
for step in range(5):
    result = v * P ** step
    plot_data.append(np.array(result).flatten())

plot_data = np.array(plot_data)
print(plot_data)


# 下面这种更容易理解， 也就是咱们先把初始状态添加进去，然后接下来在预测四种状态
# self_data = []
# self_data.append(np.array(v))
# for step in range(4):
#     result = v * P    # 当前状态乘转移概率 算出下一个状态
#     self_data.append(np.array(result).flatten())
#     v = result
# print(self_data)


# 将图形画出来
plt.figure(1)
plt.xlabel('Steps')
plt.ylabel('Probaility')
lines = []
# 六种状态，六种表示形式
for i, shape in zip(range(6), ['x', 'h', 'H', 's', '8', 'r+']):
    line, = plt.plot(plot_data[:, i], shape, label="S{}".format(i+1))
    lines.append(line)
plt.legend(handles=lines, loc=1)
plt.show()


# 这里画的是从3状态开始一直到第六个状态，概率最大的一组
temp = []
for i in range(5):
    temp.append(np.argmax(plot_data[i, :]))
print(temp)
for i, p in zip(range(6), temp):
    plt.scatter(i, temp[i]+1)
plt.show()


