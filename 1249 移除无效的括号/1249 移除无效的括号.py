#label: stack/string difficulty: medium

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.append(i)
                    
        res = ""        
        for i, ch in enumerate(s):
            if i not in stack and i not in remove:
                res += ch
        return res


