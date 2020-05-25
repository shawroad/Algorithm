"""

@file  : 003-约瑟夫环问题.py

@author: xiaolu

@time  : 2020-05-20

"""
'''
约瑟夫环问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
从编号为k的人开始报数，数到k的那个人被杀掉；他的下一个人又从1开始报数，数
到k的那个人又被杀掉；依此规律重复下去，直到圆桌周围的人只剩最后一个。
'''


def josephus(n, k):
    '''
    :param n: n个人
    :param k: 数到k被杀死
    :return:
    '''
    if k == 1:
        print('survive:', n)
        return
    p = 0
    people = list(range(1, n + 1))
    while True:
        if len(people) == 1:
            break
        p = (p + (k-1)) % len(people)
        print('killed:', people[p])
        del people[p]
    print('survive:', people[0])


if __name__ == '__main__':
    josephus(10, 4)
    josephus(10, 2)
    josephus(10, 1)