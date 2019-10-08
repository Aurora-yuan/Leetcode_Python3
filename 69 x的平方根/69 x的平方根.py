#label: 二分查找 difficulty: easy

"""
解题思路：

题目并不要求计算sqrt(x)的精确值，只需返回小于等于sqrt(x)的最大整数即可。

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo <= hi:
          mid = (hi + lo) // 2
          v = mid * mid
          if v < x:
            lo = mid + 1
          elif v > x:
            hi = mid - 1
          else:
            return mid
        return hi
