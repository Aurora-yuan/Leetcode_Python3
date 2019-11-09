#label: design difficulty: easy

"""
思路：

一道简单的栈题。

正常操作比如PUSH, POP, TOP用普通栈A操作，getmin需要借助另一个栈B来记录当前最小值。

当新元素PUSH进A时，

  （1）如果当前B为空栈，就把A也push进B

   (2) 如果当前B不为空，就比较B的栈顶和新元素的大小，把小的那一方PUSH进B

这样可以保证对于任意时刻的栈A，栈B的栈顶元素都是栈A元素的最小元素。

当A需要POP元素时，A和B同时POP。

"""

class MinStack(object):
 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        
 
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] <= x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        
 
    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        
 
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
 
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
 
 
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

