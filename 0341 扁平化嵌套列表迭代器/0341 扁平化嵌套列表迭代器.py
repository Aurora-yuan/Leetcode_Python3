#label: stack difficulty: medium

"""
第一种思路：

先把它全部展开好，然后在调用next的时候逐项输出。

"""

class NestedIterator(object):
 
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = []
        for item in nestedList:
            self.list += self.make(item)
        self.idx = 0
        print self.list
        
    def make(self, item):
        if item.isInteger():
            return [item.getInteger()]
        tmp = []
        for i in item.getList():
            tmp += self.make(i)
        return tmp
    
    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.list[self.idx - 1]
        
 
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.list)  

"""
第二种思路：

利用栈后进先出的性质，每次要next的时候通过循环处理保证栈顶为数字。

"""

class NestedIterator(object):
 
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        if nestedList:
            self.stack = nestedList[::-1]
        else:
            self.stack = []
    
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            top = self.stack.pop()
            while not top.isInteger():
                self.stack += top.getList()[::-1]
                if self.stack:
                    top = self.stack.pop()
                else:
                    return False
            self.stack.append(top)
            return True
        else:
            return False

