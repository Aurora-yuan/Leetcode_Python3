#label: 二分查找 difficulty: easy
"""
第一种思路：

先把两个数组都转成set，然后取一下交集，最后输出结果的list形式即可。

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums_1 = set(nums1)
        nums_2 = set(nums2)
        return list(nums_1 & nums_2)
        
"""
第二种思路：

先都排好序，然后选一个数组，线性扫描里面的元素，判断每个元素在不在另一个数组里，

判断的过程用二分查找实现。
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = set()
        for item in nums1:
            if self.exist(nums2, item):
                res.add(item)
        return list(res)
    
    def exist(self, nums, i):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (right + left) / 2
            if nums[mid] > i:
                right = mid - 1
            elif nums[mid] < i:
                left = mid + 1
            else:
                return True
        return False

