"""

@file  : 003-进化算法解决旅行商问题.py

@author: xiaolu

@time  : 2019-08-30

"""
import matplotlib.pyplot as plt
import numpy as np


class GA(object):
    def __init__(self, DNA_size, cross_rate, mutation_rate, pop_size):
        '''
        :param DNA_size: DNA的尺寸
        :param cross_rate: 交叉率
        :param mutation_rate: 突变率
        :param pop_size: 种群中个体数
        '''
        # 这里的DNA这样表示　　如有三个城市, 我们的三个点表示每个城市　所以有以下六种走法　012, 021, 120, 102, 201, 210
        self.DNA_size = DNA_size
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.pop_size = pop_size
        # 产生初始种群个体
        self.pop = np.vstack([np.random.permutation(DNA_size) for _ in range(pop_size)])

    def translateDNA(self, DNA, city_position):
        '''
        :param DNA: 所有种群中个体的DNA 是一个numpy矩阵
        :param city_position: 所有城市的坐标
        :return:
        '''
        # 将DNA
        line_x = np.empty_like(DNA, dtype=np.float64)  # empty_like返回一个和输入矩阵shape相同的array
        line_y = np.empty_like(DNA, dtype=np.float32)
        for i, d in enumerate(DNA):
            city_coord = city_position[d]
            line_x[i, :] = city_coord[:, 0]   # 计算个体到每个城市的横坐标距离
            line_y[i, :] = city_coord[:, 1]   # 计算个体到每个城市的纵坐标距离
        return line_x, line_y

    def get_fitness(self, line_x, line_y):
        '''
        计算适应度
        :param line_x: 当前每个个体距离每个城市的横坐标的距离
        :param line_y: 当前每个个体距离每个城市的纵坐标的距离
        :return:
        '''
        total_distance = np.empty((line_x.shape[0],), dtype=np.float32)
        for i, (xs, ys) in enumerate(zip(line_x, line_y)):
            total_distance[i] = np.sum(np.sqrt(np.square(np.diff(xs) + np.square(np.diff(ys)))))

        fitness = np.exp(self.DNA_size * 2 / total_distance)   # 每个个体之间的路径差扩大

        return fitness, total_distance

    def select(self, fitness):
        '''
        择优　选距离更小的
        :param fitness: 适应度
        :return:
        '''
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness/fitness.sum())

        return self.pop[idx]

    def crossover(self, parent, pop):
        '''
        交叉
        :param parent: 种群个体
        :param pop: 种群个体
        :return:
        '''
        if np.random.rand() < self.cross_rate:
            i_ = np.random.randint(0, self.pop_size, size=1)
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)
            keep_city = parent[~cross_points]
            swap_city = pop[i_, np.isin(pop[i_].ravel(), keep_city, invert=True)]
            parent[:] = np.concatenate((keep_city, swap_city))
        return parent

    def mutate(self, child):
        '''
        变异
        :param child:
        :return:
        '''
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, self.DNA_size)
                swapA, swapB = child[point], child[swap_point]
                child[point], child[swap_point] = swapB, swapA
        return child

    def evolve(self, fitness):
        '''
        进化
        :param fitness: 适应度
        :return:
        '''
        pop = self.select(fitness)
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop


class TravelSalesPerson(object):
    # 主要是画图
    def __init__(self, n_cities):
        self.city_position = np.random.rand(n_cities, 2)   # 随机生成所有城市的坐标
        plt.ion()

    def plotting(self, lx, ly, total_d):
        plt.cla()
        plt.scatter(self.city_position[:, 0].T, self.city_position[:, 1].T, s=100, c='k')  # 画出城市的那些点
        plt.plot(lx.T, ly.T, 'r-')
        plt.text(-0.05, -0.05, 'Total distance=%.2f'% total_d, fontdict={'size': 20, 'color': 'red'})
        plt.xlim((-0.1, 1.1))
        plt.ylim((-0.1, 1.1))
        plt.pause(0.01)


if __name__ == '__main__':
    N_CITIES = 20     # DNA的尺寸
    CROSS_RATE = 0.1   # 交叉率
    MUTATE_RATE = 0.02   # 突变率
    POP_SIZE = 500   # 种群中个体的数目
    N_GENERATIONS = 500   # 迭代500次

    ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)

    env = TravelSalesPerson(N_CITIES)

    for generation in range(N_GENERATIONS):
        lx, ly = ga.translateDNA(ga.pop, env.city_position)   # 种群　当前的城市距离
        fitness, total_distance = ga.get_fitness(lx, ly)
        ga.evolve(fitness)
        best_idx = np.argmax(fitness)
        print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx],)
        env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])

    plt.ioff()
    plt.show()
