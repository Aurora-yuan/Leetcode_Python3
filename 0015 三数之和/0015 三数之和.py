#label: 双指针 difficulty: medium


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #固定a，用双指针法在排序数组中找两数之和为-a
        nums.sort()
        l = len(nums)
        res = []
        for i, a in enumerate(nums):
            if i == 0 or nums[i] > nums[i-1]:
                left,right = i+1,l -1
                while left < right:
                    s = a + nums[left]+ nums[right]
                    if s == 0:
                        tmp = [a, nums[left],nums[right]]
                        res.append(tmp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
        return res

