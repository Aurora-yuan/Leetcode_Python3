#label: 二分查找 difficulty: easy

"""
第一种思路：

暴力解，先插入target，然后去重，转list，排序，查找target的index即可。
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return sorted(list(set(nums + [target]))).index(target)

"""
第二种思路：

二分查找
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        lo,hi = 0, len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        
        
“”“
第三种思路：

按题目要求实际上就是要：

如果target存在，找target元素的下标，因为数组已经按顺序排好，找到第一个==target元素的下标即可

如果target不存在，如果target不插在数组末尾，那么就是第一个> target元素的下标，比如[1, 3,5]插入2之后变成[1,2,3,5]

如果target应该插在数组末尾， 直接返回数组长度

”“”

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

