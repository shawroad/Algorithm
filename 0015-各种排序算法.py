"""

@file   : 0015-各种排序算法.py

@author : xiaolu

@time1  : 2019-05-31

"""

def insert_sort(array):
    # 直接插入排序
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while array[j] > temp:
            array[j+1] = array[j]
            # 从零开始存值的 所以如果array[0]比当前的值还大，j在移动就越界,所以加个判断，如果到零，立马让其强制退出本循环
            if j == 0:
                break
            j -= 1

        if j == 0:   # j退到零 这样给其存值
            array[j] = temp
        else:
            array[j+1] = temp
    return array

def Bubble_sort(array):

    # 第一层for控制比较次数
    for i in range(len(array)-1, -1, -1):
        # 第二层for控制比较
        sign = False
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                sign = True
        if sign is False:
            break
    return array


def Quick_sort(array, low, high):
    # 快速排序
    i, j = low, high
    if low > high:
        return

    if low < high:
        temp = array[low]

        while i != j:
            while i < j and array[j] > temp:
                j -= 1
            if i < j:
                array[i] = array[j]
                i += 1

            while i < j and array[i] < temp:
                i += 1
            if i < j:
                array[j] = array[i]
                j -= 1
        array[i] = temp

    Quick_sort(array, i+1, high)
    Quick_sort(array, low, i-1)

    return array


def select_sort(array):
    # 简单选择排序
    # 第一个for控制要找几次  10个数排序只需找九次  因为你把前几个最小的放好了，那第十个数也就放好了
    for i in range(len(array)):
        k = i
        min_ = array[k]
        for j in range(i, len(array)):
            if array[j] < min_:
                min_ = array[j]
                k = j
        temp = array[i]
        array[i] = min_
        array[k] = temp
    return array


def shell_sort(array):
    # 希尔排序
    # 增量分别取{5, 3, 1}
    for delta in [5, 3, 1]:
        # 里面类似于一个简单选择排序 只不过是每个delta的元素进行简单选择
        for i in range(0, len(array), delta):
            min_ = array[i]
            k = i
            for j in range(i, len(array), delta):
                if array[j] < min_:
                    min_ = array[j]
                    k = j
            temp = array[i]
            array[i] = min_
            array[k] = temp
    return array

# 归并排序分两步 1:分段 2:归并+排序
def fen_duan(array):
    # 分段
    if len(array) <= 1:
        return array
    zhong = int(len(array) / 2)
    left = fen_duan(array[:zhong])   # 一直递归下去进行分段直到剩下一个数
    right = fen_duan(array[zhong:])
    result = merge(left, right)
    return result


def merge(left, right):
    # 合并段+排序
    i, j = 0, 0
    array = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        elif left[i] > right[j]:
            array.append(right[j])
            j += 1
    if i < len(left):
        array += left[i:]
    if j < len(right):
        array += right[j:]
    return array


# 下面是堆排序的算法(本次采用大顶堆)  # 一个是排序  一个是调整堆
def Sift(array, low, high):
    # 调整堆
    i = low
    j = 2*i   # 当前这个双亲的左孩子开始调整树
    temp = array[i]
    while j <= high:
        if j < high and array[j] < array[j+1]:   # 如果右孩子大,则将j指向右孩子
            j += 1
        if temp < array[j]:    # 此时双亲小于右孩子  则右孩子和双亲换位置
            array[i] = array[j]
            i = j          # 修改i和j的值, 以便继续向下调整
            j = 2*i
        else:
            break
    array[i] = temp

def heapSort(array):
    # 堆排序
    for i in range(len(array)//2-1, -1, -1):   # len(a)//2-1 是最后一个双亲节点的索引 倒序进行调整
        Sift(array, i, len(array)-1)
    for i in range(len(array)-1, -1, -1):
        # 将根节点取出来 因为根是最大值  将根和最后一个节点交换位置
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        Sift(array, 0, i-1)  # 接着又从i-1调整树
    return array


if __name__ == '__main__':
    # 随便给定一系列数然后进行排序
    array = [3, 1, 32, 112, 4, 12, 95, 23, 25, 32]

    # 直接插入排序
    # result = insert_sort(array)
    # print("直接插入排序结果:", result)

    # 冒泡排序
    # result = Bubble_sort(array)
    # print("冒泡排序的结果:", result)

    # 快速排序
    # result = Quick_sort(array, 0, len(array)-1)
    # print("快速排序的结果:", result)

    # 简单选择排序
    # result = select_sort(array)
    # print("简单选择排序:", result)

    # 希尔排序
    # result = shell_sort(array)
    # print("希尔排序的结果:", array)

    # 归并排序
    # result = fen_duan(array)
    # print("归并排序的结果:", result)

    # 堆排序
    # result = heapSort(array)
    # print("堆排序的结果:", result)
