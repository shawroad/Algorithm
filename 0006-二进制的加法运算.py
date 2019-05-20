def binary_add(a, b):
    a = list(a)
    b = list(b)
    i = len(a) - 1
    j = len(b) - 1
    sum, temp = 0, 0
    result = []
    while i >= 0 or j >= 0:
        sum = temp
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        result.insert(0, sum % 2)
        temp = sum // 2
    return result


if __name__ == '__main__':
    a = '110110010101010010100010111111001'
    b = '1010011001011111101110100111'
    # a = '10101'
    # b = '111'
    result = binary_add(a, b)
    print(result)