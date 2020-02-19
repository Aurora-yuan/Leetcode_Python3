#label: 贪心算法 difficulty: medium

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # https://blog.csdn.net/qq_28327765/article/details/84434412
        if nums == []:
            return False
        reach = []
        for i in range(len(nums)):
            reach.append(i + nums[i])
        curr = 0
        max_reach = reach[0]
        while curr < len(nums) and curr <= max_reach:
            if reach[curr] > max_reach:
                max_reach = reach[curr]
            curr += 1
        return curr == len(nums)


