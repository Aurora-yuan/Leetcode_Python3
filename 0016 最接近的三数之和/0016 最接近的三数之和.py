#label: 双指针 difficulty: medium

"""
思路：

LeetCode-Python-15. 三数之和的简化版。

数据不强不用去重，直接一重外循环+内部双指针O（N ^ 2）可以过。

"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                s = num + nums[left] + nums[right]
                # print s, res, abs(s - target), abs(res - target)
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res


