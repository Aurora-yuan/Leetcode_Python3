#label: array difficulty: medium

"""
思路：

问连续子数组的题，首先考虑用前缀和数组解决。

找到前缀和数组之后，这道题就变成了求前缀和数组里，两数之差为k的组合个数。

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pre_sum = 0
        record = defaultdict(int)
        record[0] = 1
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            res += record[pre_sum - k]
            record[pre_sum] += 1
         
        return res

