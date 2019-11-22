#label: stack difficulty: easy

"""
思路：

s代表当前的子字符串， 用l，r来统计子字符串的左右括号个数，

当r == l的时候，就说明当前的子字符串符合原语化的要求，就可以直接把最外层的一对括号删掉，然后添加到答案里。

"""

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list()
        l,r = 0, 0
        res = ""
        for i, x in enumerate(S):
            if x == "(":
                s.append(x)
                l += 1
            elif x == ")":
                r += 1
                if l == r:         
                    res += "".join(s[1:]) #s[0]和新来的x= ")"刚好构成最外层的"()"，所以不要它们就好啦       
                    s = list()
                else:
                    s.append(x)
     
        return res

