"""

@file   : 0021-水仙花数.py

@author : xiaolu

@time   : 2019-07-05

"""
def find_shuxianhua():
    count = 0
    result = []
    for i in range(100, 1000):
        b, s, g = list(str(i))
        # print(b, s, g)
        if i == (int(b) ** 3 + int(s) ** 3 + int(g) ** 3):
            result.append(i)
            count += 1

    return result, count


if __name__ == '__main__':
    result, count = find_shuxianhua()
    print("总共有{}个水仙花数".format(count))
    print("水仙花数是:", result)

