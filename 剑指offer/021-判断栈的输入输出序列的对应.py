"""

@file   : 021-判断栈的输入输出序列的对应.py

@author : xiaolu

@time   : 2019-08-07

"""
'''
题目:
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈
序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
import copy


def is_output_stack_seq(input_stack, detect_seq):
    '''
    检测是否为出栈序列
    :param input_stack: 入栈序列
    :param detect_seq: 出栈序列
    :return: 符合:True, 否则: False
    '''
    if len(detect_seq) != len(input_stack):
        return False

    temp_stack = []
    for i in input_stack:
        temp_stack.append(i)
        while len(temp_stack) and temp_stack[-1] == detect_seq[0]:
            temp_stack.pop(-1)
            detect_seq.pop(0)
    if len(temp_stack):
        return False
    return True


if __name__ == '__main__':
    # 入栈顺序
    input_stack = [1, 2, 3, 4, 5]

    # 待测的出栈序列
    detect_seq1 = [4, 5, 3, 2, 1]
    detect_seq2 = [4, 3, 5, 1, 2]

    detect_seq = copy.deepcopy(detect_seq1)
    if is_output_stack_seq(input_stack, detect_seq):
        print("{}是{}的出栈序列。".format(detect_seq1, input_stack))
    else:
        print("{}不是{}的出栈序列。".format(detect_seq1, input_stack))
