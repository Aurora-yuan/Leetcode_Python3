#label: array difficulty: difficult

"""
思路：

对于处于1~n之间的数，把它们放到nums[i - 1]的位置上，

然后从前遍历看有没有值不等于下标加一的元素，第一个这样的元素的下标+1就是答案。

如果没有就说明当前的数字刚好覆盖了1~n， n是nums的长度。

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1
        
        return len(nums) + 1

