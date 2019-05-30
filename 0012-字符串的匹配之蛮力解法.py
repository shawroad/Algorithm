"""

@file   : 0012-字符串的匹配之蛮力解法.py

@author : xiaolu

@time1  : 2019-05-29

"""
def find_str_index(S, P):
    # 找P串在S串中的位置
    i, j, k = 0, 0, 0

    while i < len(S) and j < len(P):
        if S[i] == P[j]:
            i += 1
            j += 1
        else:
            k += 1
            i = k
            j = 0
    if j >= len(P):
        return k
    else:
        return -1


if __name__ == '__main__':
    S = 'BBCABCDABABCDABCDABDE'
    P = 'ABCDABD'
    index = find_str_index(S, P)
    print("P串在S串的位置为:", index)

