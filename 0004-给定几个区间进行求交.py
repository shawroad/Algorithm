def sort(con):
    # 1.把每个区间按后一个值进行排序  这里采用冒泡的思想
    for i in range(len(con)-1, -1, -1):
        sign = False
        for j in range(0, i):

            if con[j][1] > con[j+1][1]:
                temp = con[j][1]
                con[j][1] = con[j+1][1]
                con[j+1][1] = temp
                sign = True
        if sign == False:
            break
    return con

def concrete(sort_con):
    # 接着我们进行区间的合并

    # 1.我们判断前一个区间的第二值和后一个区间的第一个值
    i = 0
    while i <= (len(sort_con)-2):
        if sort_con[i][0] >= sort_con[i+1][0]:
            # 这个说的就是前一个区间的左端点都大于后一个区间的左端点  说明前一个区间在后一个区间的里面
            # 这个是时候的处理就是删掉前一个区间
            sort_con.remove(sort_con[i])
            continue
        elif sort_con[i][1] >= sort_con[i+1][0]:    # 此时我们再比较前一个区间的右端点是否大于后一个区间的左端点
            # 如果成立 进行合并
            temp = [sort_con[i][0], sort_con[i+1][1]]  # 前一个区间的左和后一个区间的右合成一个新区间
            sort_con.remove(sort_con[i])
            sort_con.remove(sort_con[i])   # 删除i为后，后一个元素往前移动 也就变成了第i位元素
            sort_con.insert(i, temp)
            continue
        else:
            i += 1
    return sort_con

if __name__ == '__main__':
    # 下面列表中给出了一些区间， 我们现在进行求交
    con = [[2, 5], [1, 3], [5, 9], [10, 29], [12, 20]]
    # con = [[4, 6], [2, 5], [5, 9], [1, 6], [8, 17], [4, 9], [11, 20]]
    sort_con = sort(con)
    print(sort_con)   # 按照区间的第二值进行排序  不会漏到一些点

    result = concrete(sort_con)
    print(result)