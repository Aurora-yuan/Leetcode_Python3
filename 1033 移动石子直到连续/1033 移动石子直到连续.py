#label: 脑筋急转弯 difficulty: easy

"""
思路：

先把a,b,c按从小到大的顺序排个序，然后分析一下，

最小移动次数要么是1， 要么是2。

1的情况对应最大或者最小的数距离中间数为2，那么只需要移动另一个距离中间数不为2的数即可。

2的情况对应一盘情况，把最大的数移到中间数+1，最小的数移到中间数-1。

最大移动次数就更简单了，每次挪一步就好。比如[1,3,9]，9 8 7 6 5 4这么一步步挪过来。

"""

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l = [a, b, c]
        l.sort()
        minmove, maxmove = 0, 0
        if l[0] + 1 != l[1]:
            minmove += 1
            maxmove += l[1] - l[0] - 1
        if l[1] + 1 != l[2]:
            minmove += 1
            maxmove += l[2] - l[1] - 1
        if l[1] - l[0] == 2 or l[2] - l[1] == 2:
            minmove = 1
        return [minmove, maxmove]


