"""

@file  : 002-进化算法找匹配的字符串.py

@author: xiaolu

@time  : 2019-08-30

"""
import numpy as np


class GA(object):
    def __init__(self, DNA_size, DNA_bound, cross_rate, mutation_rate, pop_size):
        '''
        :param DNA_size: DNA序列的长度
        :param DNA_bound: DNA中的取值范围
        :param cross_rate: 交叉率
        :param mutation_rate: 变异率
        :param pop_size: 种群中个体数目
        '''
        self.DNA_size = DNA_size
        DNA_bound[1] += 1  # 考虑到取尾的时候 不能取到我们设置的数
        self.DNA_bound = DNA_bound
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.mutate_rate = mutation_rate
        self.pop_size = pop_size

        self.pop = np.random.randint(*DNA_bound, size=(pop_size, DNA_size)).astype(np.int8)   # 随机初始化一批种群

    def translateDNA(self, DNA):
        # 将DNA转为对应的字符串
        return DNA.tostring().decode('ascii')

    def get_fitness(self):
        # 得到适应度 这里看个体与目标串的匹配程度
        match_count = (self.pop == TARGET_ASCII).sum(axis=1)
        return match_count

    def select(self):
        # 择优
        fitness = self.get_fitness() + 1e-4
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness / fitness.sum())
        return self.pop[idx]

    def crossover(self, parent, pop):
        # 交叉
        if np.random.rand() < self.cross_rate:
            i_ = np.random.randint(0, self.pop_size, size=1)                        # select another individual from pop
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)   # choose crossover points
            parent[cross_points] = pop[i_, cross_points]                            # mating and produce one child
        return parent

    def mutate(self, child):
        # 突变
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutate_rate:
                child[point] = np.random.randint(*self.DNA_bound)  # choose a random ASCII index
        return child

    def evolve(self):
        # 进化
        pop = self.select()
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop


if __name__ == '__main__':
    TARGET_PHRASE = 'You get it!'  # 目标字符串 这一次将DNA编码为32到126的数字 长度为字符串的长度
    POP_SIZE = 300  # 种群个体的大小
    CROSS_RATE = 0.4  # 交叉匹配率
    MUTATION_RATE = 0.01  # 突变率
    N_GENERATIONS = 1000   # 繁衍1000代

    DNA_SIZE = len(TARGET_PHRASE)
    TARGET_ASCII = np.fromstring(TARGET_PHRASE, dtype=np.uint8)  # 将字符串转为数字序列
    ASCII_BOUND = [32, 126]   # 取出ascii中这些数字对应的字符

    ga = GA(DNA_size=DNA_SIZE, DNA_bound=ASCII_BOUND, cross_rate=CROSS_RATE,
            mutation_rate=MUTATION_RATE, pop_size=POP_SIZE)

    for generation in range(N_GENERATIONS):
        fitness = ga.get_fitness()
        best_DNA = ga.pop[np.argmax(fitness)]
        best_phrase = ga.translateDNA(best_DNA)
        print('Gen', generation, ': ', best_phrase)
        if best_phrase == TARGET_PHRASE:
            break
        ga.evolve()

