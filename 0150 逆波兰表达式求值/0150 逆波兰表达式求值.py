#label: stack difficulty: medium

"""
思路：

首先声明一个栈stack，然后线性扫描input数组，

如果当前元素是运算符，就把栈的最上面两个元素进行相应运算，把它们俩弹出来，再把运算结果push进栈，

如果当前元素不是运算符，直接push就行了。

注意最后返回的结果要转换成int的形式，

而且除法需要只保留整数位。

看答案学会了 if A elif B elif C elif D 可以写成 if i in [A,B,C,D]的形式。

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ["+", "-", "*", "/"]:
                if item == "+":
                    temp = int(stack[-2]) + int(stack[-1])
                elif item == "-":
                    temp = int(stack[-2]) - int(stack[-1])
                    # print temp                
                elif item == "*":
                    temp = int(stack[-2]) * int(stack[-1])             
                elif item == "/":
                    temp = int(float(stack[-2])/ float(stack[-1]))                    
                stack.pop()
                stack.pop()
                stack.append(temp)
                
            else:
                stack.append(item)
                
        return int(stack[0])


