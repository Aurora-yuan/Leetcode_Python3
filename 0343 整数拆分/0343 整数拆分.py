#label: dynamic programming difficulty: medium

"""
https://blog.csdn.net/qq_34331113/article/details/103934114

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        integer,Break = [0,1,2],[0,1,1]
        for i in range(3,n+1):
            integer.append(i)
            ma,n = 1,i-1
            temp = 0
            while m <= n:
                break_val = max(integer[m],Break[m]) * max(integer[n],Break[n])
                if break_val > temp:
                    temp = break_val
                m += 1
                n -= 1
            Break.append(temp)
        return Break[-1]

