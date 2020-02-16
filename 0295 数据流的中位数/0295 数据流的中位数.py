#label: heap difficulty: hard

"""
思路：

用一个大顶堆和一个小顶堆来维护数据，

每次每个数进来，先把它丢进小顶堆，然后把小顶堆的堆顶丢进大顶堆，

调整两个堆，使得size 差最大为1。

这么搞的好处在于，小顶堆是数据流里前一半大的数，大顶堆是数据流里后一半的大的数，(注意：大顶堆的堆顶比小顶堆的堆顶小)

而且小顶堆的size一定 >= 大顶堆的size，

小顶堆的堆顶M是小顶堆里最小的数，大顶堆的堆顶N是大顶堆里最大的数，

如果两个堆的size相同，那么中位数就是return (M + N) / 2.0 

否则，return M / 1.0。

注意python没有大顶堆，所以放进大顶堆的数乘了-1， 取出来的时候也要记得 * -1。

"""

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = list()
        self.max_h = list()
        heapify(self.min_h)
        heapify(self.max_h)
        

    def addNum(self, num: int) -> None:
        heappush(self.min_h,num)
        heappush(self.max_h,-heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h,-heappop(self.max_h))

    def findMedian(self) -> float:
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        if max_len == min_len: #有两个候选中位数
            return (self.min_h[0] + -self.max_h[0]) / 2.
        else:#小顶堆的size 一定 >= 大顶堆的size，所以答案就是小顶堆的堆顶
            return self.min_h[0] / 1.

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
