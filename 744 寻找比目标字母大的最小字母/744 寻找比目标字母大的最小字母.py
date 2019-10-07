#label: 二分查找 difficulty: easy
"""
第一种思路：

线性扫描整个数组，如果遇到比target大的item就直接返回item，

如果过程中没有遇到比target大的就说明应该返回letters[0]

"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # lo, hi = 0, len(letters) - 1
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        return letters[0]

"""
第二种思路：

二分查找，先把极端情况去掉然后查找。
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
       
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        l, h = 0, len(letters) - 1
        while l < h:
            m = (l + h) // 2
            if letters[m] > target:
                h = m
            else:
                l = m + 1
        return letters[l]
