#label: graph difficulty: medium
 
"""
思路：

本题需要用拓扑排序解题，

拓扑排序的流程如下：

1. 找到一个入度为0的结点

2. 删除这个节点，并把这个节点相邻的结点的入度 - 1

重复这两步，直到所有的节点都被删除 或者 找不到更多的入度为0的结点 为止。

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        if not prerequisites: #没有前置课的要求
            return True
        
        indegree = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        
        for end, start in prerequisites:
            indegree[end] += 1 #统计入度
            adj[start].add(end)#生成邻接表
        
        queue = deque()
        for i, x in enumerate(indegree):
            if not x: #入度为0的结点入队
                queue.append(i)
        
        cnt = 0
        while queue:
            cur = queue.popleft() # cur 出队并删除
            cnt += 1 #当前的cur满足条件
            
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1 #邻居入度- 1
                if not indegree[neighbor]: #如果邻居入度变成了0了，就让它入队
                    queue.append(neighbor)
    
        return cnt == numCourses #判断是不是所有的点都删除成功了

