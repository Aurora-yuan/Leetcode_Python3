#label: array difficulty: easy

"""
思路一：

数据规模是40，000，所以O(N^2)是不行滴，稳定超时，

那么就用哈希表实现O(N）的算法吧，开辟一个defaultdict的哈希表， key是多米诺骨牌的值，value是这种多米诺骨牌出现的频率，

然后线性遍历输入数组，每次查找已经出现过的等价的多米诺骨牌的频率，查找完成后把当前的多米诺骨牌的频率 + 1。

注意处理当多米诺骨牌的两个值相等时的特殊情况。

"""

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        res = 0
        for i,x in enumerate(dominoes):
            if x[0] != x[1]:
                res += dic[(x[0],x[1])] + dic[(x[1],x[0])]  #该句在dic[(x[0],x[1])] += 1保证了未出现过的频率为0
            else:
                res += dic[(x[0],x[1])]
            dic[(x[0],x[1])] += 1
        return res
        
 “”“
思路二：

如果把每个多米诺骨牌的值排好序，那么就不用考虑两个值相等的特殊情况了。
 
 ”“”
 
 class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        res = 0
        for i, x in enumerate(dominoes):
            pair = (x[1], x[0])
            if x[0] < x[1]:
                pair = (x[0], x[1])
            res += dic[pair]
            dic[pair] += 1
            
        return res

