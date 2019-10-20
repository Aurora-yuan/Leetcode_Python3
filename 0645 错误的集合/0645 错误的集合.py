#label: maths difficulty: easy

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = [0 for i in range(1, len(nums)+1)]
        
        for i, digit in enumerate(nums):
            n[digit - 1] += 1
                
        for i, x in enumerate(n):
            if x == 2:
                twice = i + 1
            elif x == 0:
                never = i + 1
                
        return [twice, never]


