#label: 二分查找 difficulty: medium

"""
思路：

先用二分查找找到旋转的分界点，比如[4,5,6,7,0,1,2]的7， 特点是这一位比后一位大。

找到之后数组就分成了两段单调递增的区间，将target跟nums[0]比较之后可以判断出target落在哪段区间上，

然后就是普通的二分查找。

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            # print mid, nums[mid]
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]:
                break
            if nums[mid] < nums[-1]:
                hi = mid - 1
            elif nums[mid] >= nums[0]:
                lo = mid + 1
                
        if lo > hi:#没有旋转
            lo, hi = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                lo, hi = 0, mid
            else:
                lo, hi = mid + 1, len(nums) - 1
 
        while(lo <= hi):
            # print lo, hi
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1


