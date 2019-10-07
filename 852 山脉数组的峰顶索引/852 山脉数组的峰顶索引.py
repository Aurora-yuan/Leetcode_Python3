#label: 二分查找 difficulty: easy
"""
第一种思路：

根据题意，A中一定有一个最大值点作为山顶，而且要求输出的就是这个最大值点的坐标，那么一行就可以解决。
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))

"""
第二种思路：

二分查找，找到最大值所在的位置，

线性扫描整个数组，设置left， right 分别指向数组头尾，每次扫描都更新mid，

如果mid处于递增区间，就代表还没有到山顶，因此更新left，

如果mid处于递增区间，同样地更新right。
"""

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A)-1
        
        while(left <= right):
            mid = int(left + (right-left)/2)
            if A[mid-1] < A[mid] < A[mid+1]:
                left = mid + 1
            elif A[mid-1] > A[mid] > A[mid+1]:
                right = mid - 1
            else:
                break
                
        return mid
