#label: string difficulty: easy

"""
思路

首先想到运用两个指针一起遍历，各一个指针name[i] 与 typed[j] 相同时，同时后移，不相同时，

判断 typed[i-1] 是否与 typed[j] 相同（和前一个比较字符比较是否重复了），相同则将j 后移，不相同返回false
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j = 0,0
        while i<len(name) and j<len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j] and i>0:
                j+= 1
            else:
                return False
        
        if name[-1] == typed[-1]:
            return True
        else:
            return False
