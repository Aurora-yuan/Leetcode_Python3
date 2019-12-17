#label: sort difficulty: medium

"""
思路：

先把intervals按照interval.start从小到大的顺序排好序，

（intervals = sorted(intervals,key=lambda x:x.start) 这一行代码是从评论区学来的）

用left和right 作为当前的左端点和右端点，

每次扫描到一个新的元素时item，如果item.start比right小，则说明当前的item可以被合并，新的合并区间的右端点应该为item.end和right的最大值，

如果item.start比right大，则说明item不能被合并，需要将left和right添加到答案里，然后重置为item.start, item.end

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or not intervals[0]:
            return intervals
        
        intervals = sorted(intervals, key = lambda x:x[0])
 
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            
            if s <= end: # overlap
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e 
 
        res.append([start, end])
        return res


