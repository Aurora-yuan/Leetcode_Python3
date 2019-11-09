#label: design difficulty: easy

class MyHashSet(object):
    #桶排序的思想
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [0 for _ in range(1000005)]
 
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashmap[key] = 1
        
 
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashmap[key] = 0
        
 
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.hashmap[key] == 1
 
 
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


