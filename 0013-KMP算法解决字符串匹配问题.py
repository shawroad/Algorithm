"""

@file   : 0013-KMP算法解决字符串匹配问题.py

@author : xiaolu

@time1  : 2019-05-29

"""
def getNext(P):
    # 获取Next数组
    i, j = 1, 0
    Next = [0 for i in range(len(P))]    # 初始化一个Next数组
    Next[0] = len(P)
    Next[1] = 0
    while i < Next[0]-1:
        if j == 0 or P[i] == P[j]:
            i += 1
            j += 1
            Next[i] = j
        else:
            j = Next[j]
    return Next


def KMP(S, P):
    # 开始匹配
    Next = getNext(P)
    i, j = 1, 1
    while i < len(S) and j < len(P):
        if j == 0 or S[i] == P[j]:
            i += 1
            j += 1
        else:
            j = Next[j]
    if j >= len(P):
        return i - len(P)
    else:
        return 0


if __name__ == '__main__':
    S = 'BBCABCDABABCDABCDABDE'
    S = list(S)
    S.insert(0, len(S))   # 将长度添加到第一个位置
    P = 'ABCDABD'
    P = list(P)
    P.insert(0, len(P))   # 将长度添加到第一个位置
    index = KMP(S, P)
    print(index)
