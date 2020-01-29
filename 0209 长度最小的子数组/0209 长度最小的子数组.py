#label: 双指针 difficulty: medium

"""
思路：

sliding window, 用双指针lo, hi 维护区间，如果区间和小于 s， 说明还需要更多的元素，则hi 往右移，

如果区间和大于s， 说明可以尝试减少元素来得到最短的满足条件的区间，则lo往右移。

"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
             return 0
        res = 2 << 31
        lo, hi = 0, 0
 
        while(hi < len(nums) and lo <= hi):           
            if sum(nums[lo:hi + 1]) < s:
                hi += 1
            elif sum(nums[lo:hi + 1]) >= s:
                res = min(res, hi - lo + 1)        
                lo += 1
 
                # print nums[lo: hi + 1]
 
        return res if res != 2 << 31 else 0

