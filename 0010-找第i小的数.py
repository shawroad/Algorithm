def quick_sort(data, low, high):
    '''
    一趟快排的实现
    :param data:原本的数据
    :param low: 头
    :param high: 尾
    :return: 返回一趟快排中间的索引
    '''
    i = low
    j = high
    if low < high:
        temp = data[low]
        while i < j:
            while i < j and data[j] > temp:
                j -= 1
            if i < j:
                data[i] = data[j]
                i += 1
            while i < j and data[i] < temp:
                i += 1
            if i < j:
                data[j] = data[i]
                j -= 1

        data[i] = temp
    return i

def select_min_s(data, s, low, high):
    if s-1 == low:
        return data[low]
    if s-1 == high:
        return data[high]

    index = quick_sort(data, low, high)

    if s-1 == index:
        return data[index]
    elif s-1 < index:
        return select_min_s(data, s, low, index-1)
    else:
        t_index = (s-1) - index
        return select_min_s(data, t_index, index+1, high)

if __name__ == '__main__':
    data = [46, 43, 23, 12, 4, 423, 43, 23, 5, 34, 53, 45]
    # 找出第5小的数
    s = 5
    # 1.先进行一趟快排
    low = 0
    high = len(data)-1
    min_s = select_min_s(data, s, low, high)
    print(min_s)