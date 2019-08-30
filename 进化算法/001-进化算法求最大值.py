"""

@file  : 001-进化算法求最大值.py

@author: xiaolu

@time  : 2019-08-30

"""
import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 10            # DNA的长度　DNA length
POP_SIZE = 100           # 种群个数(种群中有多少人) population size
CROSS_RATE = 0.8         # DNA的80%进行交叉配对,20%不变
MUTATION_RATE = 0.003    # 基因突变的比例
N_GENERATIONS = 200      # 繁衍多少代
X_BOUND = [0, 5]         # X轴的坐标范围


def F(x):
    # 找这个函数的最大值
    return np.sin(10*x)*x + np.cos(2*x)*x


def get_fitness(pred):
    # 计算适应度　在这里就相当于高度　1e-3是为了按概率选择时,避免分母为０
    return pred + 1e-3 - np.min(pred)  # 减min是为了防止负数


def translateDNA(pop):
    # 将DNA翻译成数字　　二进制转十进制 并归一化
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * X_BOUND[1]


def select(pop, fitness):
    # 优胜略汰
    # 随机选择　但是按概率的  返回选中的个体
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness / fitness.sum())

    return pop[idx]


def crossover(parent, pop):
    # 交叉
    # crossover(parent, pop_copy)
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)     # 随机选取一个个体
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)    # 选择交叉的点　把哪些点变了
        parent[cross_points] = pop[i_, cross_points]    # 生成一个孩子
    return parent


def mutate(child):
    # 变异
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child


if __name__ == '__main__':

    # 初始化种群的DNA
    pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))
    plt.ion()
    x = np.linspace(*X_BOUND, 500)  # 画图
    plt.plot(x, F(x))

    for _ in range(N_GENERATIONS):
        F_values = F(translateDNA(pop))  # 翻译得到高度

        if 'sca' in globals():
            sca.remove()

        sca = plt.scatter(translateDNA(pop), F_values, s=200, lw=0, c='red', alpha=0.5)
        plt.pause(2)

        fitness = get_fitness(F_values)  # 算适应度　相当于在高度上加了一些东西
        print('最乖的宝宝:', pop[np.argmax(fitness), :])

        # 择优
        pop = select(pop, fitness)

        pop_copy = pop.copy()
        for parent in pop:
            child = crossover(parent, pop_copy)
            child = mutate(child)
            parent[:] = child

    plt.ioff()
    plt.show()


