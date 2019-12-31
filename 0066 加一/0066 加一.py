#label: list difficulty: easy

"""
思路：

先翻转，然后给第零个元素 + 1，

再处理进位。

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = digits[::-1]
        l[0] += 1
        for i in range(len(digits)):
            if l[i] > 9:
                l[i] -= 10
                if i != len(digits) - 1:
                    l[i+1] += 1
                else:
                    l.append(1)
        return l[::-1]

