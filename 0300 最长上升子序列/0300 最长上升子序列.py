#label: dynamic programming difficulty: medium


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if not l:
            return 0
        dp = [1 for _ in range(l)]
        
        for i in range(1,l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
                    
        return max(dp)
