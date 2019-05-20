def is_boundry(top, buttom, left, rigth):
    if top >= buttom  or left >= rigth:
        return True
    else:
        return False


def print_luoxuan(matrix):
    top = 0
    buttom = len(matrix)
    left = 0
    right = len(matrix[0])
    while True:
        # 访问上行  从左到右
        for i in range(left, right):
            print(matrix[top][i])
        top += 1
        if is_boundry(top, buttom, left, right):
            break
        # 访问右列  从上到下
        for i in range(top, buttom):
            print(matrix[i][right-1])
        right -= 1
        if is_boundry(top, buttom, left, right):
            break
        # 访问下行   从右到左
        for i in range(right-1, left-1, -1):
            print(matrix[buttom-1][i])
        buttom -= 1
        if is_boundry(top, buttom, left, right):
            break
        # 访问左列   从下到上
        for i in range(buttom-1, top-1, -1):
            print(matrix[i][left])
        left += 1
        if is_boundry(top, buttom, left, right):
            break

if __name__ == '__main__':
    # 给定一个矩阵 螺旋式输出该矩阵
    matrix = [[3, 4, 1, 6, 1, 3, 7],
              [3, 23, 43, 2, 4, 4, 2],
              [43, 53, 23, 53, 3, 2, 5],
              [5, 3, 2, 5, 23, 34, 2]]

    print_luoxuan(matrix)