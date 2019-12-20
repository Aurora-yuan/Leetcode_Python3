#label: dfs + 回溯算法 difficulty: medium

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(tmp, nums):
            if not nums:
                res.append(tmp)
                    
            for i, x in enumerate(nums):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(tmp + [x], nums[:i] + nums[i + 1:])
                
        dfs([], nums)
        return res


