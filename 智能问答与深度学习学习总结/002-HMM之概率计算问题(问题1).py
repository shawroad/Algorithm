"""

@file   : 002-HMM之概率计算问题(问题1).py

@author : xiaolu

@time   : 2019-07-08

"""
# 隐马尔可夫有三个问题
# 问题1: 已知模型参数和观测序列，计算该观测序列出现的概率，属于概率计算问题
# 问题2: 已知观测序列和模型参数，找出一个最有可能的隐藏状态序列，属于预测问题
# 问题3: 根据观测到的序列集找到一个最后可能的HMM, 属于学习问题

states = ('健康', '感冒')   # 状态序列
observations = ('正常', '发冷', '发烧')    # 观测序列
start_probability = {"健康": 0.6, "感冒": 0.4}   # 初试状态的概率

# 转移概率
trans_probability = {
    "健康": {"健康": 0.7, "感冒": 0.3},
    "感冒": {"健康": 0.4, "感冒": 0.6}
}

# 喷射概率
emission_probability = {
    "健康": {"正常": 0.5, "发冷": 0.4, "发烧": 0.1},
    "感冒": {"正常": 0.1, "发冷": 0.3, "发烧": 0.6}
}


# 前向算法
def forward(obs):
    fwd = [{}]
    # 初始化t = 0
    for y in states:
        # 算的是第一个观测值“正常”的概率
        fwd[0][y] = start_probability[y] * emission_probability[y][obs[0]]
    # print(fwd)   # [{'健康': 0.3, '感冒': 0.04000000000000001}]

    for t in range(1, len(obs)):
        # 从第二个观测值开始算起
        fwd.append({})
        for y in states:
            fwd[t][y] = sum((fwd[t-1][y0] * trans_probability[y0][y] * emission_probability[y][obs[t]]) for y0 in states)
    # print(fwd)
    prob = sum(fwd[len(obs) - 1][s] for s in states)
    return prob


# 后向算法
def backward(obs):
    bwk = [{} for t in range(len(obs))]
    T = len(obs)
    for y in states:
        bwk[T-1][y] = 1
    # print(bwk)    # [{}, {}, {'健康': 1, '感冒': 1}]
    for t in reversed(range(T-1)):
        for y in states:
            print(y)
            # 当前计算 == 后一个状态(两种状态) 乘 当前状态转向后一种状态的概率 乘 后一种状态喷射出后一种观测的概率
            bwk[t][y] = sum((bwk[t+1][y1] * trans_probability[y][y1] * emission_probability[y1][obs[t+1]]) for y1 in states)
    prob = sum((start_probability[y] * emission_probability[y][obs[0]] * bwk[0][y]) for y in states)
    return prob


if __name__ == '__main__':
    # 前向算法
    prob1 = forward(observations)
    print("前向算法: 出现'正常', '发冷', '发烧'的概率", prob1)

    # 后向算法
    prob2 = backward(observations)
    print("后向算法: 出现'正常', '发冷', '发烧'的概率", prob2)


