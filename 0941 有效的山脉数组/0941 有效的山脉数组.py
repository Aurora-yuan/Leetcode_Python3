#label: array difficulty: easy

"""
思路：

题目要求如下：

1. 长度 > 3

2. 可以分成两段，第一段严格递增，第二段严格递减。（严格的意思是不能出现重复）

3. 最高点不能是第一个点或者最后一个点。

找到两段之后，用转集合比较长度的方法判断有没有重复元素，

再用排序的方法判断是不是严格递增和严格递减。

"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        max_pos = A.index(max(A))
        if max_pos in [0,len(A)-1]:
            return False
        first,last = A[:max_pos+1],A[max_pos:]
        if len(first) != len(set(first)) or len(last) != len(set(last)): #判断是否有重复元素
            return False
        return first == sorted(first) and last == sorted(last)[::-1]
        
