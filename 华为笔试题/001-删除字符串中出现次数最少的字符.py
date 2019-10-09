"""

@file  : 001-删除字符串中出现次数最少的字符.py

@author: xiaolu

@time  : 2019-10-09

"""
'''
给定一个字符串, 去除字符串中的低频字符
'''
import collections


if __name__ == '__main__':
    # 建立有序字典
    v_c = collections.OrderedDict()

    # s = input("请输入字符串:")
    s = 'fdjaopgjpajgofdsjalngdaf'
    for i in s:
        v_c[i] = v_c.get(i, 0) + 1

    min_count = 1000

    for v, i in v_c.items():
        if i < min_count:
            min_count = i
    print(min_count)

    low_freq_v = []
    for v, i in v_c.items():
        if i == min_count:
            low_freq_v.append(v)
    print(low_freq_v)

    result = ''
    for i in s:
        if i not in low_freq_v:
            result += i
    print("最终的结果:", result)











