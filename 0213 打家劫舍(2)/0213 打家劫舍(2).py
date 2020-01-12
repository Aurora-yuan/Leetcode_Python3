#label: dynamic programming difficulty: medium

"""

思路：

类似：LeetCode-Python-198. 打家劫舍

区别在于1号房屋和最后一号房屋只能二选一，

所以只要算出去掉1号房屋之后198的解， 和去掉最后一号房屋之后198的解，然后两者取大即可。

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob2(nums[1:]),self.rob2(nums[:-1]))
    
    def rob2(self,nums):
        if not nums:
            return 0

        dp = [0 for _ in nums]
        dp[0] = nums[0] 
        # dp[1] = max(nums[0],nums[1])
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


