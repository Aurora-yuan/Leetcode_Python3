#label: maths difficulty: easy

"""
思路一：

转集合，然后遍历0 ~ n 看在不在集合里。
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for num in range(len(nums)):
            if num not in s:
                return num
        return len(nums)
        
“”“
第二种思路：

数学法，把 0 ~ n的数字之和，减去sum（nums），即可得到缺失数的值。

”“”
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) /2 - sum(nums)
        
“”“
第二种思路：

位运算法，利用xor的性质 A ^ A = 0, 把nums里的所有的下标 和 元素的值都xor一下，即可得到缺失数。

注意res需要初始化为 len(nums)， 因为 下标最大只会为 len（nums） -  1。

”“”

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
