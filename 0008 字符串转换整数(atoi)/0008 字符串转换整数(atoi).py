#label: string difficulty: medium

"""
思路：

这题不难，就是坑有点多：

1. 先把开头所有的 “ ”给去掉

2. 现在合法的第一个元素只有 + - 和数字，把不合法的排除掉

3. 用一个运算符op来记录一下结果的正负号

4. 在处理第一个元素的时候解决op的问题

5. 如果遇到元素为空或者不是数字，就说明合法的数字已经结束了

6. 最后判断一下结果是否在合法范围内

"""

class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip(" ")
        if not len(s): #排除空
            return 0
        if s[0] not in ["+", "-"] and not s[0].isdigit(): #排除第一个非空字符不是数字
            return 0
        op = 1
        res = ""
        for i, char in enumerate(s):
            if i == 0 :
                if char == "-":
                    op = -1
                    continue
                elif char == "+":
                    continue
            if char == " " or not char.isdigit():
                break
            res += char
        # print res, op
        if len(res) > 0:
            res = op * int(res)
        else:
            return 0
        INT_MIN = -2 **31
        INT_MAX = 2 **31 - 1
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        return res


