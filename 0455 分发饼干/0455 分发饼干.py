#label: 贪心算法 difficulty: easy

"""
思路：

先把两个数组都排好序，然后线性顺序扫描，

如果按顺序某个孩子可以被满足，那么就满足他，这里就是贪心的体现，因为数组已经排序，所以这个孩子可以被满足就代表着用这个饼干就行了，没必要用后面更大的饼干，

如果饼干不能满足当前的孩子，就尝试下一个更大的饼干，

直到某个数组结束为止。

"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while(child<len(g) and cookie<len(s)):
            if (g[child] <= s[cookie]):
                child += 1
            cookie += 1
        return child
            

