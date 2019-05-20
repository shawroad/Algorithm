def find_n_k(n, k):

    # 首先进行累乘，算出当n等于几，有多少种组合
    fact = [0]*(n+1)  # 这里面
    fact[0] = 1  # 不从零个数开始  底下的for直接从1开始，然后到n
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i
    # print(fact)  #[1, 1, 2, 6, 24, 120, 720, 5040]  可以看到第一个(实际第2个)位置是1，也就是一个数只有一种组合，
    #  第二个位置是2  也就是两个数有两种组合。  第三个位置时6，也就是说三个数有6中组合


    temp = [0]*n
    for i in range(1, n+1):
        temp[i-1] = i

    result = []
    k -= 1
    # 下面是核心思想
    for i in range(1, n):

        index = k // fact[n-i]

        result.append(temp[index])

        temp.remove(temp[index])
        k -= (index*fact[n-i])
    result.append(temp[0])
    return result


if __name__ == '__main__':

    n = 4   # 则总共有7!种组合
    k = 12   # 我们要在7!种找到第k个组合输出
    result = find_n_k(n, k)
    print('第{}个序列为:{}'.format(k, result))