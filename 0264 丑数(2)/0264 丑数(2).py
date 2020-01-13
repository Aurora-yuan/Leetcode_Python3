#label: math difficulty: medium

"""
思路：

思考一下可以发现，除第一个丑数1外，每个丑数都可以由之前的丑数 * 2 或3 或5 得到，

比如 1 * 2 = 2， 1 * 3 = 3， 1 * 5 = 5， 2 * 2 = 4， 2 * 3 = 6， 2 * 5 = 10。。。。。

所以找到所有的丑数很简单，挨个乘 2 或3 或5即可，

下一步要确定如何按顺序找到丑数，

显然，丑数的顺序遵循从小到大的顺序，因此可以理解为动态找最小值，

所以用最小堆就可以实现，

注意，因为会出现 2 * 3 = 6 和 3 * 2 = 6的情况，所以需要开一个set避免重复。

"""

from heapq import *

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        l = [1]
        heapify(l)
        cnt = 1
        used = set([1])
        while cnt < n:
            cur = heappop(l)
            if cur * 2 not in used:
                heappush(l,cur*2)
                used.add(cur*2)
            if cur * 3 not in used:
                heappush(l,cur*3)
                used.add(cur*3)
            if cur * 5 not in used:
                heappush(l,cur*5)
                used.add(cur*5)
            cnt += 1
        return heappop(l)
