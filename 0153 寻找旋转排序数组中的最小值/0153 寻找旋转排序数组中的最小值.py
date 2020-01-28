#label: 二分查找 difficulty: medium

"""
第一种思路：

线性扫描找最小值， O（N）

第二种思路：

二分查找找最小值， O（logN）

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: #处理0个元素
            return 0
        if len(nums) == 1: #处理1个元素
            return nums[0]
        
        if nums[0] < nums[-1]: #没发生旋转
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if mid + 1< len(nums): #mid 不是最后一位
                if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]: #找到了
                    return nums[mid]
            else:
                if nums[mid - 1] > nums[mid]: # mid 是最后一位
                    return nums[mid]
                
            if nums[mid] < nums[-1]: 
                right = mid - 1
            else:
                left = mid + 1


