#label: sort difficulty: medium

"""
解题思路：

将nums数组原地排序，然后把排序后的后一半放在奇数位置，前一半放在偶数位置。注意，存放时要降序放置，否则[4,5,5,6]这种情况不满足题意。

"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])
        nums[::2],nums[1::2] = nums[:mid][::-1],nums[mid:][::-1]

