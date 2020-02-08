#label: array difficulty: medium

"""
思路：

使用列表存储元素值，使用字典存储元素值及其在列表中的索引。重点关注删除操作：先将要删除的val对应的索引值赋给列表中最后一个元素，

接下来对列表中两个元素进行交换，最后在列表和字典中分别移除val即可。

"""

class RandomizedSet(object):
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.index = {}
 
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        self.values.append(val)
        self.index[val] = len(self.values)-1
        return True
 
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        self.index[self.values[-1]] = self.index[val]
        self.values[-1],self.values[self.index[val]] = self.values[self.index[val]],self.values[-1]
        self.values.pop()
        self.index.pop(val)
        return True
 
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randint(0,len(self.values)-1)]
 
 
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


