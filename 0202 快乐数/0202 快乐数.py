#label: maths difficulty: easy

"""
思路：

照着要求算就行了，开辟一个list来储存之前出现过的值，如果当前值之前已经出现过，就说明陷入循环，肯定不可能变成1。

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while n and n not in visited:
            visited.add(n)
            tmp = self.happy(n)
            if tmp == 1:
                return True
            n = tmp
 
        return False

    def happy(self,num):
        res = 0
        while num:
            num, tmp = divmod(num, 10)
            res += tmp ** 2
        return res
 
