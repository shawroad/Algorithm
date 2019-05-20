def big_data_mult(a, b):
    a = list(a)
    b = list(b)
    # 把a拿着和b的每一位去乘 ，每乘一次， 结果向左移一位()

    # 列表的头插list.insert(0, item)
    temp = []
    temp_sub = []  # 存的是每次a与b中一位乘的结果
    for i in range(len(b)-1, -1,  -1):
        if len(b)-1 == i:  # 第一下乘 不需要移位
            pass
        else:
            # 插入k个零
            k = 1
            while k <= len(b) - 1 - i:
                temp_sub.insert(0, 0)
                k += 1
        for j in range(len(a)-1, -1, -1):
            # 拿b中一位与a中所有为进行相乘
            temp_sub.insert(0, int(b[i]) * int(a[j]))
        temp.append(temp_sub)
        temp_sub = []
    return temp

def fill_list(max_len, temp):
    temp_fill = []

    for item in temp:
        if len(item) < max_len:
            i = 0
            n = len(item)
            while i < max_len - n:
                item.insert(0, 0)
                i += 1
        temp_fill.append(item)
    return temp_fill

def get_result(temp_fill, maxlen):
    result = [0] * (max_len+1)

    # 将各列先累加起来 等会处理进位
    for i in range(max_len-1, -1, -1):
        for item in temp_fill:
            # 对因为累加起来  最后考虑进位
            result[i+1] += item[i]

    # 现在处理进位
    for i in range(len(result)-1, -1, -1):
        if result[i] >= 10:
            result[i-1] += result[i] // 10
            result[i] = result[i] % 10

    return result


if __name__ == "__main__":
    # a作为乘数， b作为被乘数
    a = '45755564532435735465878576'
    b = '8765434234657373'
    # 拿着b中的数与a中的每一位去乘
    temp = big_data_mult(a, b)

    # 现在的任务是找出temp中最长的那个串，将其他不够的进行填充   其实不用找了 肯定是temp的最后一个
    max_len = len(temp[-1])  # 找出了最长。然后在其他的头部填充，将其所有元素的长度搞成一致的

    temp_fill = fill_list(max_len, temp)
    # 这个打印的是填充好的所有行
    print("打印填充好的数组:\n")
    for i in temp_fill:
        print(i)
    # 将其对应位累加即可
    result = get_result(temp_fill, max_len)
    print('最后的运算结果:\n',result)