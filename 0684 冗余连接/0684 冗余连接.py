#label: 并查集 difficulty:medium

"""
思路：

用并查集依次插入每条边,

如果一条边的两个端点在插入这条边之前能找到相同的root，就说明这条边插入后会形成环。

找到满足条件的最后一条边返回即可。

"""

class UnionFindSet(object):
    def __init__(self, edges):
 
        # m, n = len(grid), len(grid[0])
        self.roots = [i for i in range(1001)]
        self.rank = [0 for i in range(1001)]
        self.count = 0
 
    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        # for root in tmp:
        #     self.roots[root] = member
        return member
        
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufs = UnionFindSet(edges)
        res = []
        for edge in edges:
            x,y = edge[0],edge[1]
            p,q = ufs.find(x),ufs.find(y)
            if p == q:
                res = edge
            else:
                ufs.union(p,q)
                
        return res
