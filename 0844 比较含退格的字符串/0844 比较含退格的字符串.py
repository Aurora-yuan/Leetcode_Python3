#label：stack difficulty: easy

"""
注意字符串开始是#的情况
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        import operator
        stack1 = []
        stack2 = []
        for s in S:
            if s != '#':
                stack1.append(s)
            else:
                if len(stack1) == 0:
                    continue
                else:
                    stack1.pop()
        for t in T:
            if t != '#':
                stack2.append(t)
            else:
                if len(stack2) == 0:
                    continue
                else:
                    stack2.pop()
                    
        return operator.eq(stack1,stack2)
        
