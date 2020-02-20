#label: 贪心算法 difficulty: medium

"""
https://blog.csdn.net/qq_32424059/article/details/90114006

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        for i in range(len(gas)):
            if i < idx: #如果在某一站被卡住了，那么从它之前的所有站出发都不行
                continue
                
            j = i
            left_gas = gas[i]
            while left_gas > 0:
                if left_gas < cost[j]: #去不了下一站
                    idx = max(idx, j) #这一站有毒，必须从这一站之后出发才行
                    break
                left_gas -= cost[j] #去下一站
                if (j + 1) % len(gas) == i: #走了一圈了
                    return i
                
                j = (j + 1) % len(gas)
                left_gas += gas[j]
        return -1


