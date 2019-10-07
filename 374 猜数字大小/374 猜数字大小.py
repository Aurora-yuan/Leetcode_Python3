#label:二分查找 difficulty: easy
"""
二分查找。注意guess返回的结果，如果是-1，说明猜大了，下一次应该猜更小的数字，

如果是1，说明猜小了，下一次应该猜更大的数字。

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo,hi = 1,n
        while(lo<=hi):
            mid = lo+(hi-lo)//2
            val = guess(mid)
            if val == 1:
                lo = mid+1
            elif val == -1:
                hi = mid - 1
            else:
                return mid
