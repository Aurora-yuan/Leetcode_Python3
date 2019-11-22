#label: stack difficulty: easy

class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        #暴力查找即可
        if not findNums or not nums:
            return []
        res = list()
        for item in findNums:
            index = nums.index(item)
            for i in range(index, len(nums)):
                if nums[i] > item:
                    res.append(nums[i])
                    break
            if i + 1 == len(nums) and nums[-1] <= item:
                res.append(-1)
        return res


