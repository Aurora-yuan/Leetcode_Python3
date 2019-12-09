#label: stack difficulty: medium

"""
思路：

开辟一个栈stack来模拟入栈出栈的操作，对于pushed里的每一个元素，都进行一次入栈，

入栈之后比较当前的栈顶和队列头是否相同，如果相同，则栈顶和队头同时POP。

当pushed里的每一个元素都扫描结束时，如果stack为空，说明pushed和popped数组匹配成功，返回True；如果不为空，就说明不对，返回False。

"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while(stack and popped[i] == stack[-1]):
                stack.pop()
                i += 1
        return stack == []

