"""

@file   : 031-全排列.py

@author : xiaolu

@time   : 2020-01-17

"""
class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    result = sol.permute(nums)
    print(result)
