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

class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        if x < 4:
            return 1
        start,end = 2, x//2
        while 1:
            i = (start+end) // 2
            if i ** 2 <= x and (i+1) **2 > x:
                return i
            if i ** 2 < x:
                start = i+1
            if i ** 2 > x:
                end = i -1
