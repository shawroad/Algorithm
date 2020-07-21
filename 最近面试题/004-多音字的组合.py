# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:15
# @Author  : xiaolu
# @FileName: 004-多音字的组合.py
# @Software: PyCharm
def dfs(data):

    result = []

    def digui(s, index):
        if index == len(data):
            result.append(s)
            return

        temp = data[index]
        for t in temp:
            digui(s + t, index + 1)

    digui('', 0)
    return result


if __name__ == '__main__':
    # data = [['zhao', 'chao'], ['yang'], ['men'], ['qian', 'gan'], ['long']]
    data = [['1'], ['2', '3'], ['4', '5', '6']]
    result = dfs(data)
    print(result)