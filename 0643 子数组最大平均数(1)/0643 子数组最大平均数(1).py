#label: array/滑动窗口 difficulty: easy

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = -99999
        res = -99999
        for i in range(len(nums) - k + 1):
            if s == -99999:
                s = sum(nums[:k])
            else:
                s -= nums[i - 1]
                s += nums[i + k - 1]
            res = max(res, s / k)
            
        return res
                

