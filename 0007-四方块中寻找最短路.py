def short_path(mat):
    i = len(mat)    # 行数
    j = len(mat[0])  # 列数
    # 建立一个标志矩阵  代表着我们当前往哪里走
    sign = [[None for k in range(j)] for m in range(i)]
    sign[0][0] = '起点'
    for k in range(1, j):
        mat[0][k] += mat[0][k-1]
        sign[0][k] = '向左'
    for m in range(1, i):
        mat[m][0] += mat[m-1][0]
        sign[m][0] = '向上'
    for k in range(1, j):
        for m in range(1, i):
            temp = min(mat[m-1][k], mat[m][k-1])
            if temp == mat[m-1][k]:
                sign[m][k] = '向上'
            if temp == mat[m][k-1]:

                sign[m][k] = '向左'
            mat[m][k] += temp
    for item in sign:
        print(item)

    return mat, sign

def print_path(sign):

    path = []
    i = len(sign) -1
    j = len(sign[0])-1
    while i > 0 and j > 0:
        if sign[i][j] == '向左':
            j -= 1
            path.append('向左')
        if sign[i][j] == '向上':
            i -= 1
            path.append('向上')
    path.append('起点')

    return path

if __name__ == '__main__':
    matrix = [[2, 3, 1, 4, 4],
              [2, 1, 4, 5, 3],
              [3, 0, 2, 3, 6],
              [4, 3, 2, 0, 8],
              [4, 2, 0, 2, 1]]
    mat, sign = short_path(matrix)

    # 打印路径
    path = print_path(sign)
    print("从终点会起点的路径:", path)