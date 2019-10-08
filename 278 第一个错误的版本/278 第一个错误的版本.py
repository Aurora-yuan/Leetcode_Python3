#label: 二分查找 difficulty: easy
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分查找左侧边界
        left,right = 1,n
        while left < right:
            mid = left + (right-left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
