#label: 回溯算法 difficulty: medium

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                if item not in result:
                    result.append(item[:])
        return result
    


