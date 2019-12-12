#label: graph/Dijkstra difficulty: medium

"""

思路

寻找源到目标的最低花费，Dijkstra 是一个好的算法。

Dijstra 算法的基本思想就是：按照 cost 从小到大的顺序扩展所有可能的飞行路线，当城市被添加到 dst 时，dst 中对应的值就是到达该城市的最低花费。

算法

在 Dijkstra 算法中，借助优先级队列持续搜索花费最低的下一个城市。

如果查找到某个城市，它原本的路线成本更低或者中转次数过多，则无需再搜索它。否则，如果搜索到目的城市，那么当前花费就是最低成本，

因为每次最先搜索的就是最低成本航线。

否则，如果从 node 城市出发的航线花费更低，则将该节点加入到优先级队列用于搜索。

"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1


