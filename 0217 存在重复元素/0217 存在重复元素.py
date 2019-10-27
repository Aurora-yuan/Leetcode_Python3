#label: hash table difficulty: easy


"""
思路一：

用hashmap记录出现过的元素。
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = dict()
        for num in nums:
            if record.get(num,0):
                return True
            else:
                record[num] = 1
        return False
        
“”“
思路二：

转集合，看长度有没有变化。

”“”

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

“”“
思路三：

collection.counters()函数

“”“
