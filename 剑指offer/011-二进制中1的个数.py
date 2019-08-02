"""

@file   : 011-二进制中1的个数.py

@author : xiaolu

@time   : 2019-07-31

"""
def convert_binary(d):
    # 正数转二进制
    result = []
    while d > 0:
        yushu = d % 2
        d = d // 2
        result.insert(0, yushu)
    return result


def convert_binary_neg(d):
    # 负数转二进制
    result = []
    while d > 0:
        yushu = d % 2
        d = d // 2
        result.insert(0, yushu)

    # 反码
    temp_result = []
    for r in result:
        if r == 0:
            temp_result.append(1)
        if r == 1:
            temp_result.append(0)
    return temp_result


def count_1(d):
    # 统计1的个数
    total_1 = 0
    for i in d:
        if i == 1:
            total_1 += 1
    return total_1


if __name__ == '__main__':
    data = [23, 12, -12, -23]
    for d in data:
        if d > 0:
            result = convert_binary(d)
            result_1_num = count_1(result)
            # print("正数:", result)
            print(result_1_num)
        else:
            d = abs(d)
            result = convert_binary_neg(d)
            result_1_num = count_1(result)
            # print("负数:", result)
            print(result_1_num)

    # 我记得好像正负数在最高位上是有标记的. 这里我就不做了 若想加标记, 直接用insert(0, data)

