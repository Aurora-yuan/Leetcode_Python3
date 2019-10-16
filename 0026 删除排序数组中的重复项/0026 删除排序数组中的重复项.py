#label: 双指针 difficulty: easy

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i < 1 or nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i


