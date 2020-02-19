#label: 贪心算法 difficulty: medium

class Solution:
    def jump(self, nums: List[int]) -> int:
        # https://blog.csdn.net/qq_28327765/article/details/84434152
        if len(nums) < 2:
            return 0
        jump_befor_end = 1 #jump_min
        pre_max_reach = nums[0]
        curr_max_reach = nums[0]
        for i in range(1, len(nums)):
            if i > curr_max_reach: # 贪心，若无法再向前移动了，才进行跳跃
                jump_befor_end += 1
                curr_max_reach = pre_max_reach
            pre_max_reach = max(pre_max_reach, i + nums[i])
        return jump_befor_end


