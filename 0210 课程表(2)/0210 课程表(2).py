#label: graph difficulty: medium

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        indegree = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        
        for end, start in prerequisites:
            indegree[end] += 1
            adj[start].add(end)
            
        from collections import deque
        queue = deque()
        
        for i, x in enumerate(indegree):
            if not x:
                queue.append(i)
                
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res if len(res) == numCourses else []

