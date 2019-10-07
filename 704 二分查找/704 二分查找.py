#label: 二分查找 difficulty: easy
"""
思路：

二分查找入门题
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<=right):
            mid = int(left+(right-left)/2)
            if nums[mid]<target:
                left = mid + 1
            elif nums[mid]>target:
                right = mid - 1
            else:
                return mid
            
        return -1
