#label: Heap difficulty: easy

"""
思路：

问第/前K个最大/最小元素就用堆，此题同理。

维护一个size为K的小顶堆，则堆顶元素即为第K大的元素。

"""

from heapq import *
class KthLargest(object):    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """  
        self.heap = nums            
        self.k = k
        heapify(self.heap) #数组建堆
        while len(self.heap) > k:
            heappop(self.heap) 
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

