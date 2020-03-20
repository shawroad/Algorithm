"""

@file   : 073-最小的K个数.py

@author : xiaolu

@time   : 2020-03-20

"""
'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
'''
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        '''
        思路就是人工做法
        :param arr:
        :param k:
        :return:
        '''
        if k > len(arr):
            return arr
        if k == 0:
            return []

        result = []
        result.extend(arr[:k])
        result.sort()
        for v in arr[k:]:
            if v < result[-1]:
                # 进行插入把最后一个淘汰
                for i, w in enumerate(result):
                    if w > v:
                        result.insert(i, v)
                        result.pop(-1)
                        break
        return result


if __name__ == '__main__':
    # arr = [3, 2, 1]
    # k = 2
    arr = [0, 1, 2, 1]
    k = 1
    sol = Solution()
    result = sol.getLeastNumbers(arr, k)
    print(result)





