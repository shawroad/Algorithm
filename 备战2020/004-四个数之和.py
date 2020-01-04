"""

@file   : 004-四个数之和.py

@author : xiaolu

@time   : 2020-01-02

"""

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        
        if not nums or n < 4:
            return []
        
        nums.sort()
        
        result = []
        
        for i in range(n - 3):
            # 防止重复  后一个数和前一个数相等
            if i > 0 and nums[i] == nums[i-1]:
                continue   
            
            # 当走到当前i位置的时候  如果最小和都比目标值大  那就break
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # 当最大值比目标值都小的话 那就是当前i位置不行  换下一个值
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            for j in range(i+1, n-2):
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue

                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break

                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                # 双指针
                L = j + 1
                R = n - 1

                while L < R:
                    tmp = nums[i] + nums[j] + nums[L] + nums[R]

                    if tmp == target:
                        result.append([nums[i], nums[j], nums[L], nums[R]])

                        while L < R and nums[L] == nums[L+1]:
                            L += 1

                        while L < R and nums[R] == nums[R-1]:
                            R -= 1

                        L += 1
                        R -= 1

                    elif tmp > target:
                        R -= 1

                    else:
                        L += 1
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    # nums = [0, 0, 0, 0]
    targets = 0
    sol = Solution()
    result = sol.fourSum(nums, targets)
    print("最终的结果:", result)



