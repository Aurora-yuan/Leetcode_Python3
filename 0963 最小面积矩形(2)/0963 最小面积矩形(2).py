#label: Geometry difficulty: medium

"""
思路：

https://www.jianshu.com/p/d53d6bee3196

"""

import itertools
import collections

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list) #seen存放相同斜率的点的中点
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2  # get the center point
            radius = abs(center - P)  # caculate the distance
            # Only record P here, because Q =  2 * center - P
            seen[center, radius].append(P)

        res = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                # caculate area
                res = min(res, abs(P - Q) * abs(P - (2 * center - Q)))

        return res if res < float("inf") else 0
