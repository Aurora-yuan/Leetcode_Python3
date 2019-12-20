#label: dfs + 回溯算法 difficulty: medium

"""
思路：

DFS+回溯。

先考虑一位的情况，然后把递归地考虑去掉这一位数后的数组的全排列。

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # 思路一： 调库
        # from itertools import permutations
        # return list(permutations(nums, len(nums)))
        res = []
        def dfs(tmp,nums):
            if not nums:
                res.append(tmp)
            for i,x in enumerate(nums):
                dfs(tmp+[x],nums[:i]+nums[i+1:])
            
        dfs([],nums)
        return res

