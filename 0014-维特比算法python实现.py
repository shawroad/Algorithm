"""

@file   : 0014-维特比算法python实现.py

@author : xiaolu

@time1  : 2019-05-30

"""
import numpy as np

def viterbi(trainsition_probability,emission_probability,pi,obs_seq):
    # params: trainsition_probability 隐状态之间的转移概率
    # params: emission_probability  每种隐状态喷射不同观察值的概率矩阵
    # params: pi 各种隐状态的初试概率值
    # params: obs_seq 随意指定了一个观察序列

    # 转换为矩阵进行运算
    trainsition_probability = np.array(trainsition_probability)
    emission_probability = np.array(emission_probability)
    pi = np.array(pi)
    obs_seq = np.array(obs_seq)

    # 最后返回一个Row*Col的矩阵结果
    Row = trainsition_probability.shape[0]
    Col = len(obs_seq)

    # 要返回的矩阵
    F = np.zeros((Row, Col))
    # 在初试 三种隐状态的初试概率乘喷射出0观察值的概率
    F[:, 0] = pi * np.transpose(emission_probability[:, obs_seq[0]])
    for t in range(1, Col):
        list_max = []
        for n in range(Row):
            # [此刻若是sunny转sunny, 此刻若是cloudy转sunny, 此刻若是windy转sunny,
            #  此刻若是sunny转cloudy, 此刻若是cloudy转cloudy, 此刻若是windy转cloudy,
            #  此刻若是sunny转windy, 此刻若是cloudy转windy, 此刻若是windy转windy]  这是一个列表  看此刻转谁更大
            list_x = list(np.array(F[:, t-1]) * np.transpose(trainsition_probability[:, n]))

            # 获取最大概率
            list_p = []
            for i in list_x:
                list_p.append(i*10000)   # 相当于保留四位小数
            list_max.append(max(list_p) / 10000)   # 获取最好的隐态
        # 然后让最好的隐状态喷射出三种观测值的概率
        F[:, t] = np.array(list_max)*np.transpose(emission_probability[:, obs_seq[t]])

    return F


if __name__ == '__main__':
    # 隐藏状态
    invisible = ['Sunny', 'Cloud', 'Rainy']

    # 初试状态
    pi = [0.61, 0.17, 0.20]

    # 转移矩阵   如第一个0.5 代表隐态从 Sunny 转 Sunny的概率
    trainsition_probability = [[0.5, 0.375, 0.125],
                               [0.25, 0.125, 0.625],
                               [0.25, 0.375, 0.375]]

    # 发射矩阵  如:第一行 代表
    emission_probability = [[0.6, 0.2, 0.15, 0.05],
                           [0.25, 0.25, 0.25, 0.25],
                           [0.05, 0.10, 0.35, 0.5]]

    # 最后显示状态  因为每一种隐状态都能喷射出各种观察值，假设我现在指定观察值是0, 2, 3
    # 维特比解决的就是这三种观察值到底是谁喷射的(也就是预测隐状态的序列)
    obs_seq = [0, 2, 3]

    # 最后返回一个Row*Col的矩阵结果
    F = viterbi(trainsition_probability, emission_probability, pi, obs_seq)
    print(F)

    # 输出结果:
    # [[ 0.378　　   0.02835　　      0.00070875]
    # [ 0.0425 　　 0.0354375 　　 0.00265781]
    # [ 0.01 　　     0.0165375 　　 0.01107422]]
    # 第一列 代表的观察值是0 则三种天气喷射出观察值0的概率
    # 第二列 代表的观察值是2 则三种天气喷射出观察值2的概率
    # 第三列 代表的观察值是3 则三种天气喷射出观察值3的概率

