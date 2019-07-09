"""

@file   : 003-HMM之预测问题(问题2).py

@author : xiaolu

@time   : 2019-07-08

"""
# 隐马尔可夫有三个问题
# 问题1: 已知模型参数和观测序列，计算该观测序列出现的概率，属于概率计算问题
# 问题2: 已知观测序列和模型参数，找出一个最有可能的隐藏状态序列，属于预测问题
# 问题3: 根据观测到的序列集找到一个最后可能的HMM, 属于学习问题


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    # 建立t0时刻个状态概率
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    # print(V)
    # print(path)
    # print("*"*100)

    # 沿着时间1, 2..t进行计算
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        # 根据t-1时刻状态概率，观测概率矩阵和转移概率矩阵计算t时刻最大概率转态 记录路径
        for y in states:
            # 看前一个状态中, 那个状态转移到当前状态并且当前状态喷射出当前观测值的概率大， 谁大谁就做前一个状态
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            # {'健康': ['健康', '健康']}  若下一句输出左边 意思是: 当前健康概率最大, 是由前一个健康转向后一个健康
            newpath[y] = path[state] + [y]  # y状态概率最大: 前一个状态 和 当前能喷射出最大概率的状态
            # print(V)
            # print(newpath)
        path = newpath
    # 最后结果：
    # [{'健康': 0.3, '感冒': 0.04000000000000001}, {'健康': 0.084, '感冒': 0.027}, {'健康': 0.00588, '感冒': 0.01512}]
    # {'健康': ['健康', '健康', '健康'], '感冒': ['健康', '健康', '感冒']}
    # 显然可以看出最后一个字典中概率最大的是0.01512  并且是感冒
    # 那我们的输出路径就是下面字典的感冒路线
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])


if __name__ == "__main__":
    states = ('健康', '感冒')  # 状态序列
    observations = ('正常', '发冷', '发烧')  # 观测序列
    start_probability = {"健康": 0.6, "感冒": 0.4}  # 初试状态的概率

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

    # viterbi(obs, states, start_p, trans_p, emit_p)
    result = viterbi(observations, states, start_probability, trans_probability, emission_probability)
    print(result)


