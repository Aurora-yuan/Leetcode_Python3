#label: graph difficulty: medium

"""
思路：

建图然后DFS搜索。

a -> b 这条路的weight 是2.0, b - > c的weight是3.0,

求a -> c的结果就是求从a出发到c的一条路径，并返回路径上所有weight 的乘积。

"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        
        for i, equation in enumerate(equations):
            start, end = equation[0], equation[1]
            graph[start].add(end) #设置从start到end 的path     
            weight[(start, end)] = values[i] #给上一行设置的path分配weight
            graph[end].add(start) #设置从end到start的path
            weight[(end, start)] = 1.0 / values[i] #给上一行设置的path分配weight
            
        # print weight    
        def dfs(start, end, visited):
            if (start, end) in weight: #如果可以直接读出结果
                return weight[(start, end)] #就直接返回
            
            if start not in graph or end not in graph: #这两个点根本没出现过
                return 0
            
            if start in visited: #已经形成路径环了还没找到结果
                return 0
            
            visited.add(start) #标记一下start来过了
            res = 0
            
            for tmp in graph[start]:#遍历所有能从start出发的路径
                res = weight[(start, tmp)] * dfs(tmp, end, visited)
                if res != 0: #找到了第一条路
                    weight[(start, end)] = res #把这一条路的weight记录下来
                    break
            visited.remove(start) #回溯
            # print res
            return res
        
        res = []
        for query in queries:
            tmp = dfs(query[0], query[1], set())
            if tmp == 0: #如果没找到
                tmp = -1.0
            res.append(tmp)
            
        return res


