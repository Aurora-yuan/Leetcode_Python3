#label: array difficulty: easy

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum,rsum = 0,sum(nums)
        for i,item in enumerate(nums):
            rsum -= item
            if lsum == rsum:
                return i
            lsum += item
        return -1
