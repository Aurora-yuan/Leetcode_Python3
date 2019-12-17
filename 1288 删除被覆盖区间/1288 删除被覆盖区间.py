#label: line sweep difficulty: medium

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        from typing import List
        size = len(intervals)
        if size < 2:
            return size

        intervals.sort(key=lambda x: x[0])

        remove_count = 0
        max_right = intervals[0][1]

        for i in range(1, size):
            if intervals[i][1] <= max_right:
                remove_count += 1
            else:
                max_right = intervals[i][1]

        return size - remove_count


