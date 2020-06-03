#label: BFS/graph difficulty: medium

"""
思路：

图的遍历BFS + 哈希表解题。

利用一个哈希表mapping记录所有的节点和它的copy的关系。

时间复杂度：O（N）

空间复杂度：O（N）

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict, deque
        mapping = dict() # key is the original node, value is its copy

        if not node:
            return None
        
        queue = deque([node])
        visited = set()
        visited.add(node)
        while queue:
            cur = queue.popleft()
            visited.add(cur)
 
            copy = Node(cur.val, [])
            mapping[cur] = copy
            for neigh in cur.neighbors:
                if neigh not in visited:
                    queue.append(neigh)
                    
        for cur, copy in mapping.items():
            for each in cur.neighbors:
                copy.neighbors.append(mapping[each])
        return mapping[node]

