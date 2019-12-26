#label: dynamic programming difficulty: medium

"""
思路：

见https://blog.csdn.net/Whyalwaysxu/article/details/87032566

"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        allSum = sum(nums)
        avg = allSum / k
        if allSum % k or max(nums) > avg:
            return False

        def DFS(i, target):
            if nums[i] == target:
                nums[i] = 0
                return True
            if nums[i] < target:
                for j in range(i-1, -1, -1):
                    if not nums[j] or nums[j] + nums[i] > target:
                        continue
                    res = DFS(j, target-nums[i])
                    if res:
                        nums[i] = 0
                        return True
            return False

        i = len(nums)-1
        nums.sort()
        while i >= 0 and nums[i]:
            res = DFS(i, avg)
            if res:
                i -= 1
                continue
            else:
                return False
        return True



