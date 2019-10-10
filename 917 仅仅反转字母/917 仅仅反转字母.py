#label: string difficulty: easy

"""
解题思路：

从两端向中间遍历字符串，如果前后两个都是字母就进行交换（由于字符串不能进行修改，所以先将字符串转换成列表），如果不是字母就比较下一个。

"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        i = 0
        j = len(s) - 1
        
        while i<j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
                
            if not s[i].isalpha():
                i += 1
            if not s[j].isalpha():
                j -= 1
            
        return "".join(s)
