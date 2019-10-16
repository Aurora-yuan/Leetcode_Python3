#label: 双指针 difficulty: easy

"""
第一种思路：

     线性扫描，把值不等于val的所有元素按顺序依次从num的开头往后放.

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 
        
 """
 第二种思路：

     倒着线性扫描，遇到值等于val的元素就把它pop掉。
 
 """
 
 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                      
        return len(nums)
