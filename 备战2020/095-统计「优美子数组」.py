"""

@file  : 095-统计「优美子数组」.py

@author: xiaolu

@time  : 2020-04-21

"""
'''
给你一个整数数组 nums 和一个整数 k。
如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中「优美子数组」的数目。
 
示例 1：
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。

示例 2：
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。

示例 3：
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, right, oddCnt, res = 0, 0, 0, 0

        l = len(nums)
        while right < l:
            # 右指针先走, 每遇到一个奇数则oddCnt++
            # 奇数 & 1等于1   偶数 & 1等于0
            if nums[right] & 1 == 1:
                # 说明是奇数
                oddCnt += 1
            right += 1

            # 若当前滑动窗口[left, right]中有k个奇数时, 进入此分支统计当前滑动窗口中的优美子数组个数
            if oddCnt == k:
                # 先将滑动窗口的右边界右拓展, 直到遇到下一个奇数(或者出界)
                tmp = right
                while right < l and nums[right] & 1 == 0:
                    right += 1

                rightEventCnt = right - tmp
                leftEventCnt = 0
                while nums[left] & 1 == 0:
                    leftEventCnt += 1
                    left += 1

                # 第一个奇数左边的leftEventCnt个偶数都可以作为优美子数组的起点
                # 第k个奇数右边的rightEventCnt个偶数都可以作为优美子数组的终点
                res += (leftEventCnt + 1) * (rightEventCnt + 1)
                left += 1
                oddCnt -= 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    sol = Solution()
    result = sol.numberOfSubarrays(nums, k)
    print(result)
