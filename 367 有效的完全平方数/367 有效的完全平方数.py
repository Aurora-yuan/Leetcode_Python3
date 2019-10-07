#label: 二分查找 difficulty: easy
"""
思路：

典型的二分查找，或者可以用Python的暴力美学 return num ** 0.5 %1 == 0
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while(left<=right):
            mid = left + (right - left) // 2
            if mid**2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid - 1
            else:
                return True
        
        return False
