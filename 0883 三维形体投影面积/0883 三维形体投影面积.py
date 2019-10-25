#label: maths difficulty: easy

"""
思路：

观察示例2可以得到结论，结果由三部分相加，

第一部分是从上往下看的面积，这其实等于数组中不为0的元素个数，

第二部分是从右前方看的面积，对应每一列的最大值，

第三部分是从左前方的对立面看的面积，对应每一行的最大值。

找矩阵的列可以用 zip(*grid)，非常好用。
"""

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        s0, s1, s2 = 0, 0, 0
        n = len(grid)
        
        for i in grid:
            s0 += n - i.count(0)
            s1 += max(i)
        
        for i in zip(*grid): #zip(*grid) 得到转置后的矩阵
            s2 += max(i)
        
        return s0 + s1 + s2

