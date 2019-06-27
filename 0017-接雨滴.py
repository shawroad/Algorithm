"""

@file   : 0017-接雨滴.py

@author : xiaolu

@time   : 2019-06-27

"""
def show(array):
    # 只是为了展示
    for i in array:
        print(i)


if __name__ == '__main__':
    # array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    array = [4, 2, 5, 3, 12, 3, 12, 5, 3, 2, 1, 3, 1]

    r = max(array)
    c = len(array)

    mat = []
    # 加下来生成一个二维矩阵
    for i in range(r):
        mat.append([0] * c)
    # show(mat)

    # 加下来按照array 给每列填充数值，
    for i, d in enumerate(array):
        for k in range(d):
            mat[k][i] = 1
    # show(mat)

    # 根据mat算雨滴
    low = 0
    high = 0
    total = 0  # 总雨点数
    for d in mat:
        for i in range(len(d)):
            if d[i] == 1:
                low = i
                break
        for j in range(len(d)):
            if d[len(d) - 1 - j] == 1:
                high = len(d) - j
                break
        i = low
        for i in range(low, high):
            if d[i] == 0:
                total += 1
        low, high = 0, 0

    print("总共的雨点数:", total)




