#label: 二分查找 difficulty: medium

"""
第一种思路：

线性扫描数组，遇到第一个count > 1 的元素就把它返回。

"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in nums:
            if nums.count(item) != 1:
                return item 

"""
第二种思路：

二分查找，已知所有数字的范围是1-n， 就可以把left设为1， right 设为n，mid设为left 和right的中间值，

每次循环，用count记录一下有多少个小于等于mid的值，

如果count <= mid，就代表重复的数字应该不会落在mid左侧的区间内，于是更新left；

反之， 就更新right。

"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        left, right = 1, len(nums) - 1
        while(left < right):
            mid = left + (right - left) /2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # print mid, count
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left





