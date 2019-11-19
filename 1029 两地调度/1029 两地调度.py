#label: 贪心算法 difficulty: easy

"""
思路：

贪心算法，先把输入数组按照两地费用之差的绝对值排好序，

从前到后线性扫描，

然后在去A市和去B市的名额都还有空余的时候，每一组费用取较小的那个，

如果去A市的名额已经满了，剩下的全部去B，

同理如果去B市的已经满了，剩下的全部去A，

"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key = lambda x: abs(x[0] - x[1]))
        costs = costs[::-1]
        a, b = 0, 0 #a, b分别代表目前去A市和去B市的人数
        n = len(costs) // 2
        res = 0
 
        for i, cost in enumerate(costs):
            if a < n and b < n:
                if cost[0] < cost[1]:
                    a += 1
                    res += cost[0]
                else:
                    b += 1
                    res += cost[1]
            elif a < n: #去B市的人数已经满了，只能去A了
                a += 1
                res += cost[0]
                
            elif b < n: #去A市的人数已经满了，只能去B了
                b += 1
                res += cost[1]
                
        return res

