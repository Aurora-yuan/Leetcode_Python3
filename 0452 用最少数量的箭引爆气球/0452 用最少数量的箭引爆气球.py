#label: 贪心算法 difficulty: medium

"""
思路：

按照区间的结束点从小到大排序

若第i个区间的起始点小于第i-1个区间的结束点，说明有重叠，可公用一支箭

反之，没有重叠，需要再用一支箭

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        p = sorted(points, key=lambda x:x[1])
        res = 1
        end = p[0][1]
        for i in range(1,len(p)):
            if p[i][0] > end:
                res+=1
                end = p[i][1]
        return res
