#label: stack difficulty: medium

"""
思路：

一般问括号都是栈，此题同理。

难点在于处理括号外的符号，比如 3+5-(3+2)中的负号，会对整个括号内的值产生影响。

所以可以用一个栈记录括号外的符号，和括号之前的运算结果。

"""

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        stack = []
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                num = 0
                sign = -1
            elif c =="(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                num = 0
                res = 0 
            elif c == ")":
                res += num * sign
                num = 0
                sign = 1
                res = res * stack.pop() + stack.pop()
        res += num * sign
        return res


