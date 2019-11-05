#label: array difficulty: easy

"""
思路：先使用sorted()函数将原列表排序，将排序后的列表与原列表中的数据一一对应，找出左边第一个不同的元素与右边起第一个不同的元素，

二者之间数据个数即为输出结果。

注意list.sort()与sorted()的区别

"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_order = list()
        nums_order = sorted(nums)
        left = len(nums)
        right = -1
        for i in range(len(nums)):
            if nums_order[i] != nums[i]:
                left = i
                break
        for i in range(len(nums)-1,0,-1):
            if nums_order[i] != nums[i]:
                right = i
                break
        if right <= left:
            return 0
        return right - left + 1
