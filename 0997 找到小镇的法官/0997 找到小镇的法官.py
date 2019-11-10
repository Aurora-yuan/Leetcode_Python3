#label: graph difficulty: easy

"""

这是一道图论题，A信任B这个关系就可以抽象为A到B的一条有向路径，题目所求的就是是否只存在一个点，使得其他所有的点都有单向路径到这个点，

而这个点无法到任何一个其他点。即找到一个入度为N-1， 出度为0的点。

开辟两个数组indegree和outdegree分别统计每个人的入度和出度，

根据trust数组往这两个数组里添加内容， trust[0]是出去的，trust[1]是进来的，

然后再从第一个人到第N个人遍历，如果有人被所有其他人信任（indegree[i] == N-1) 并且这个人谁都不相信(outdegree[i] == 0）就说明他可能是法官。

最后判断到底有几个人可能是法官，如果只有一个满足条件的法官，就返回他，否则返回 -1 。

"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
        
        res = list()
        
        for pair in trust:
            outdegree[pair[0]] += 1
            indegree[pair[1]] += 1
        
        for i in range(1, N + 1):
            if outdegree[i] == 0 and indegree[i] == N - 1:
                res.append(i)
        
        return res[0] if len(res) == 1 else -1


