"""

@file   : 002-替换空格.py

@author : xiaolu

@time   : 2019-07-30

"""
'''
题目:
    请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''
def replace_space(string):
    string_list = list(string)
    for i, c in enumerate(string_list):
        if c == ' ':
            string_list[i] = '%20'
    return ''.join(string_list)


if __name__ == '__main__':
    string = 'We Are Happy'
    # 1. 常规方法
    result = replace_space(string)
    print("原始字符创: {} \n处理后的字符串: {}".format(string, result))

    # 2. python中自带的最强方法
    # string = string.replace(' ', '%20')
    # print(string)

