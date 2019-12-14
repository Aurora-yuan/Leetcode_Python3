#label: 二分查找 difficulty: medium

"""
解题思路：

看到这种有序（或者部分有序）的数组，一般考虑使用二分查找进行优化。

开始时，左指针指向矩阵中最小元素，右指针指向矩阵中最大元素（注意：指针代表的是元素值，而不是位置），

计算矩阵中小于等于左右指针中间值的元素个数c，然后通过比较c与k的值，进行左指针或者右指针的移动。重复上述过程直到l >= r.

"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            mid = (l+r)//2
            c = sum(bisect.bisect_right(row,mid) for row in matrix) 
            # bisect.bisect_right(row,mid)计算row中元素值<=mid的数量
            if c < k:
                l = mid + 1
            else:
                r = mid
        return l


