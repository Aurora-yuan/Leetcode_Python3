#label: 双指针 difficulty: medium

"""
思路：

在LeetCode-Python-15. 三数之和的基础上再加一层循环。

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        # print n
        def threeSum(nums,t, d):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            #固定a,用双指针在排序数组里找两数之和为-a
            l = len(nums)
            res = []
            for i, a in enumerate(nums):
                if i == 0 or nums[i] > nums[i - 1]:
                #开始双指针
                    left, right = i + 1, len(nums) - 1
                    while(left < right):
                        s = a +  nums[left] + nums[right]
                        # print d, a, nums[left], nums[right]
                        if s == t:
                            tmp = [d,a, nums[left], nums[right]]
                            self.res.append(tmp)
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while right > left and nums[right] == nums[right + 1]:
                                right -= 1
                        elif s < t:
                            left += 1
                        elif s > t:
                            right -= 1
        
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] > nums[i - 1]:
                # print n[i]
                threeSum(nums[i + 1:], target - nums[i], nums[i])
                
                
        return self.res


