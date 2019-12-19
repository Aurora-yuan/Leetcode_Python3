#label: 回溯算法 difficulty: medium

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                result.append(item[:])
        return result


