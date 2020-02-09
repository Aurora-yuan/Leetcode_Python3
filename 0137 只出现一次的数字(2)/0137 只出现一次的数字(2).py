#label: dictionary/位运算 difficulty: medium

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        record = defaultdict(int)
        
        for i, x in enumerate(nums):
            record[x] += 1
        
        for key, val in record.items():
            if val == 1:
                return key


