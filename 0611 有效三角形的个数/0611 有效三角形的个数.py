#label: array difficulty: medium

"""
思路：

https://leetcode-cn.com/problems/valid-triangle-number/solution/chao-xiang-xi-pai-xu-shuang-zhi-zhen-611-you-xiao-/

"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/valid-triangle-number/solution/chao-xiang-xi-pai-xu-shuang-zhi-zhen-611-you-xiao-/
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1

        return ans
