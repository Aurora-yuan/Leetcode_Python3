#label: 二分查找 difficulty: medium

"""
思路：

首先确定存不存在，所以用一次二分查找来判断。

找到之后再用第二次二分查找往左边找左边界，找到的条件是 已经找到下标为0了 或者 找到某个target，它的左边不是target。

同理进行第三次二分查找，找右边界，找到的条件是 已经找到len(nums) - 1了 或者 找到某个target，它的右边不是target。

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo,hi = 0,len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
            
        if lo > hi:
            return [-1,-1]
        
        midtarget = mid
        lo,hi = 0,mid
        leftpos = 0
        while lo <= hi:
            if hi >= 1 and nums[hi-1] != target or hi == 0:
                leftpos = hi
                break
                
            mid = (lo + hi) // 2
            if nums[mid] == target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
                
        rightpos = 0
        lo,hi = midtarget,len(nums) - 1
        while lo <= hi:
            if lo <= len(nums) - 2 and nums[lo + 1] != target or lo == len(nums) - 1:
                rightpos = lo
                break
            mid = (lo + hi + 1) // 2
            if nums[mid] == target:
                lo = mid
            elif nums[mid] > target:
                hi = mid - 1
            
        return [leftpos,rightpos]
