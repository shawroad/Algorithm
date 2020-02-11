"""

@file   : 040-约瑟夫问题.py

@author : xiaolu

@time   : 2020-02-07

"""
'''
约瑟夫问题是个有名的问题：N个人围成一圈，从第一个开始报数，第M个将被杀掉，最后剩下一个，
                  其余人都将被杀掉。例如N=6，M=5，被杀掉的顺序是：5，4，6，2，3，1。
'''


if __name__ == '__main__':
    N = 6
    M = 5
    r = [i + 1 for i in range(N)]

    i = 0
    index = 0
    while r:
        i += 1
        index += 1
        index = index % len(r)

        if i == M-1:
            t = r.pop(index)
            print(t)
            i = 0





