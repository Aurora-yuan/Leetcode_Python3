#label: Ordered Map

"""
解题思路：

暴力法。

维护一重预订列表和双重预订列表。当预订一个新的日程安排 [start, end) 时，如果它与双重预订列表冲突，则会产生三重预定。

算法：

当且仅当事件 [s1, e1) 在另一个事件 [s2, e2) 结束后开始，两个事件不冲突，也就是说满足 e1<=s2 或 e2<=s1 时，两个事件不冲突。

这意味着当 s1<e2 和 s2<e1 时，事件发生冲突。

如果新的日程安排与双重预订冲突，则返回 false。否则，我们会将与一重预定列表冲突的时间添加到双重预订列表中，并将该预定添加到一重预定列表中。

"""

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True  
    
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)



