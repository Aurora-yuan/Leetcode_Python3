#label: graph difficulty: easy

"""
思路：

先通过paths把建立一个dictionary，key是每个花园，val是跟key相连的花园。

然后再处理每个key，把它和它的相连的花园不冲突地安排好，

因为答案一定存在，所以顺序处理下去就好了。

注意花的种类只有四种，一开始以为很多种所以疯狂超时……

"""

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        #每个花园最多和3个别的花园相连
        # if not paths:
        #     return []
        from collections import defaultdict
        dic = defaultdict(list)
        
        for path in paths:
            x0, y0 =  path[0], path[1]
            dic[x0].append(y0)
            dic[y0].append(x0)
            
        # print dic
        res = [-1 for _ in range(N + 1)]
        # print len(dic.keys())
        for i in dic.keys():
            neibors = dic[i]
            used = [0 for _ in range(5)]
            for neibor in neibors:
                if res[neibor] != -1:
                    used[res[neibor]] = 1
            if sum(used) == 0:
                res[i] = 1
            else:
                for j in range(1, 5):
                    if used[j] == 0:
                        res[i] = j
                        break
        # print res
        for i, x in enumerate(res):
            if x == -1:
                res[i] = 1
        return res[1:]
            


