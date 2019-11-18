#label: 位运算 difficulty: easy

"""
第一种思路：

最简单，直接调库

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        
“”“
第二种思路：

利用位运算 n & n - 1会消去最后一个1的性质计算。 

”“”

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            n = n & (n - 1)
        return res

