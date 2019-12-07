#label: stack/string difficulty: medium

"""
思路：

一般问括号都是栈，这题也不例外，

用栈找到最中间的括号，然后把中间部分翻转，再递归处理即可。

"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s or ")" not in s:
            return s
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                left = stack.pop()
                right = i
                return self.reverseParentheses(s[:left] + s[left + 1:right][::-1] + s[right + 1:])


