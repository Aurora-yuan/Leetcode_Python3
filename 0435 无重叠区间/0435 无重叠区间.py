#label: 贪心算法 difficulty: medium

"""
思路

题目要求需移除区间的最小数量，即求能组成不重叠区间最多的个数
因为：
能组成不重叠区间最多的interval个数 =interval总个数 - 需移除interval的最小数量

核心步骤：
（1）按照end对所有的interval进行升序排序
（2）从前往后遍历排序后的interval，若不重叠，则个数加1，否则，跳过，然后进入下一次是否重叠的比较。
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not len(intervals):
            return 0
        #按照end进行排序
        intervals = sorted(intervals, key=lambda k: k[1])
        print(intervals)
        #记录最小的end
        minEnd = intervals[0][1]
        rest = 1
        for i in range(1,len(intervals)):
            #若下一个interval的start小于minEnd,则算重叠
            if intervals[i][0] < minEnd:
                continue
            rest += 1
            minEnd = intervals[i][1]
        return len(intervals) - rest

