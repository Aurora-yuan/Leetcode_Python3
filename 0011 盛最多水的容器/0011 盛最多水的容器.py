#label: 双指针 difficulty: medium

"""
思路：

双指针法。

每次循环二者中高度小的那个指针往中心移动，因为这样可以抵消宽度减小带来的影响，更有可能得到面积更大的矩形。

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo,hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            if height[lo] > height[hi]:
                area = height[hi] * (hi - lo)
                hi -= 1
            else:
                area = height[lo] * (hi - lo)
                lo += 1
            res = max(res,area)
            
        return res
