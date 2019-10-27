#label: hast table difficulty: easy

"""
思路：

利用哈希表记录映射关系，处理一对多和多对一的两种错误。

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        for i,char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[i]: #一对多的错误
                    return False
            else:
                if t[i] in mapping.values():  #多对一的错误
                    return False
                mapping[char] = t[i]
                    
        return True
                
