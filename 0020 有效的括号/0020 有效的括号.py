#label: stack difficulty: easy

"""
非常经典的一道堆栈的题目
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ("(","[","{"):
                stack.append(char)
            elif char == ")":
                if len(stack) == 0: #栈为空
                    return False
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if len(stack) == 0: #栈为空
                    return False
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == "}":
                if len(stack) == 0: #栈为空
                    return False
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
