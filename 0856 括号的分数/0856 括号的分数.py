#label: string difficulty: medium

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        #转成十进制的表达式，然后利用eval函数计算表达式的值
        # ()代表1， ))代表)*2, )(代表+
        s = ""
        
        for i in range(len(S) - 1):
            if S[i] == "(":
                if S[i + 1] == "(":
                    s += "("
                else:
                    s += "1"
                    
            else:
                if S[i + 1] == "(":
                    s += "+"
                else:
                    s += ")*2"
                    
        # print s
        return eval(s)


