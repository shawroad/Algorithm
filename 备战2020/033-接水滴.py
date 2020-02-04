"""

@file   : 033-接水滴.py

@author : xiaolu

@time   : 2020-02-03

"""


class Solution:
    def trap(self, height):
        area = 0
        i = 0
        j = len(height) - 1
        l_highest = 0
        r_highest = 0
        pre = 0
        while i < j:
            if l_highest <= r_highest:
                while i < j and height[i] <= l_highest:
                    i += 1
            if l_highest >= r_highest:
                while i < j and height[j] <= r_highest:
                    j -= 1

            area += (min(height[i], height[j]) - pre) * (j - i + 1)

            pre = min(height[i], height[j])
            l_highest = height[i]
            r_highest = height[j]

        # 黑色  也就是柱子的面积
        area_black = 0
        for h in height:
            area_black += h

        # 总面积 - 黑色面积
        area_blue = area - area_black

        return area_blue if area_blue > 0 else 0


if __name__ == '__main__':
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = Solution()
    result = sol.trap(nums)
    print(result)

