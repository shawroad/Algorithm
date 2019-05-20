#  01 背包问题
def bag_01(weights, values, capicity):

    # [*, *, *, *, *, *, *, *, *, *, *, *]
    # [*, *, *, *, *, *, *, *, *, *, *, *]
    # [*, *, *, *, *, *, *, *, *, *, *, *]
    # [*, *, *, *, *, *, *, *, *, *, *, *]
    # [*, *, *, *, *, *, *, *, *, *, *, *]
    # [*, *, *, *, *, *, *, *, *, *, *, *]
    n = len(values)
    f = [[0 for j in range(capicity+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capicity+1):
            f[i][j] = f[i-1][j]
            if j >= weights[i-1] and f[i][j] < f[i-1][j-weights[i-1]] + values[i-1]:
                f[i][j] = f[i-1][j-weights[i-1]] + values[i-1]
    return f

def show(capicity, weights, f):
    n = len(weights)
    print("最大价值:", f[n][capicity])
    x = [False for i in range(n)]
    j = capicity
    for i in range(n, 0, -1):
        if f[i][j] > f[i-1][j]:
            x[i-1] = True
            j -= weights[i-1]
    print("背包中所装物品为:")
    for i in range(n):
        if x[i]:
            print("第{}个".format(i+1))


if __name__ == '__main__':
    # weights 指的是物品的重量
    # values 指的是物品的价值
    # capicity 指的是袋子能装的重量
    n = 5
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    capicity = 11
    m = bag_01(weights, values, capicity)
    # 打印矩阵
    for i in range(len(m)):
        print(m[i])

    # 接下来输出要装的物品
    show(capicity, weights, m)

    #
    # row = [0] * (capicity+1)
    # f = [row for i in range(len(values))]
    # # 将那个矩阵造好了
    # for i in range(1, len(f)):
    #     for j in range(2, capicity+1):
    #         if j < weights[i]:
    #             f[i][j] = f[i-1][j]
    #         else:
    #             f[i][j] = max(f[i-1][j], f[i-1][j-weights[i]]+values[i])
    #
    # return f
    #