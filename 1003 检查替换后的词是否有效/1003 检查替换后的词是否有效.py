#label: string difficulty: medium

"""
思路：

跟打祖玛一样，先从中间的abc开始消除，然后递归判断消除abc后的子字符串。

"""

class Solution:
    def isValid(self, S: str) -> bool:
        l = len(S)
        if l < 3:
            return False
        if S == "abc":
            return True
        if S[0] == "b" or S[0] == "c":
            return False
        if "abc" in S:    
            index = S.index("abc")
        else:
            return False
        # print S
        S = S[: index] + S[index + 3:]
        # print S
        return self.isValid(S)


