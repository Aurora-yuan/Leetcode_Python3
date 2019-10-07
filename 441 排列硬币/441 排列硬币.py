#label: 二分查找 difficulty: easy
"""
思路：

二分查找。

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1 +2 + 3 + ... + k = (k + 1) * k / 2 < n
        lo,hi = 0,n
        while(lo<=hi):
            mid = (lo+hi) // 2
            total = (mid+1)*mid // 2
            if total>n:
                hi = mid-1
            elif total<n:
                lo = mid+1
            else:
                return mid
        return lo-1
        
 """
 或者利用求根公式
 
 """
 
 class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # 1 +2 + 3 + ... + k = (k + 1) * k / 2 < n
        return (-1 + int(math.sqrt(1 + 8 * n))) // 2

