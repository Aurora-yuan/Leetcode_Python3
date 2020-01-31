#label：二分查找 difficulty: medium

"""
思路：

二分查找。

根据题意：找的是某个点，满足这个点的值 > = 它和它右侧的点个数之和cnt情况下，cnt就是当前的h指数

如果已经有h指数了，就可以试着往左找，因为越左cnt越大，h指数也越大，所以左侧可能存在更大的h值，

如果目前还没有h指数，就只能试着缩小cnt，往右找，

此题缩小搜索范围的思路就可以用二分查找来实现。

"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        lo, hi = 0, l - 1
        res = 0
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            cnt = l - mid #包括mid自身右边还有的元素个数
            if citations[mid] >= cnt: 
                res = cnt
                hi = mid -1
            else:
                lo = mid + 1
        return res                         


