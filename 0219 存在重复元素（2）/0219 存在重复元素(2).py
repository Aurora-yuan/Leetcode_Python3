#label: hast tabel difficulty: easy

"""
思路：

用一个dict来记录每个元素最新出现的坐标。

如果一个数跟它上一次出现的坐标的差值小于等于k。

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = dict()
        for i,num in enumerate(nums):
            if record.get(num,-1) != -1:
                if i - record[num] <= k:
                    return True
        
            record[num] = i
        
        return False
