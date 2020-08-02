# label: BFS difficulty: medium

"""
思路：

每个数字可以扭到它相邻的两个数，所以这道题可以抽象为从起点出发，判断能否到达特定的某个点，路途中不能碰到障碍。

题目问最小移动次数，BFS的特点：优先搜索离根节点近的节点， 所以用BFS来处理。

"""

from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if "0000" in deadends: #如果连起点都不能走就88
            return -1
        
        queue = deque()
        queue.append(["0000", 0])
        cnt = 0
 
        while queue:
            node, cnt = queue.popleft() #取一个点出来，cnt是当前走的步数
            if node == target: #找到了
                return cnt     
 
            for i in range(4):
                for j in [1, -1]:
                    next_node = node[:i] + str((int(node[i]) + j) % 10) + node[i + 1:] 
 
                    if next_node not in deadends: #新的点可以走而且没走过
                        deadends.add(next_node) #避免重复
                        queue.append([next_node, cnt + 1])
 
        return -1

