#label: slide window difficulty: medium

"""
思路：

先生成开销数组， record[i] = s[i]变成t[i]的开销

然后问题就可以转化为在一个数组里，求和不超过maxCost的连续子数组的最大长度。

滑动窗口可解。

"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        record = []
        for i in range(n):
            record.append(abs(ord(t[i])-ord(s[i])))
            
        start,end = 0,0
        windowsum = 0
        res = 0
        for end in range(n):
            windowsum += record[end]
            if windowsum > maxCost:
                res = max(res,end - start)
                windowsum -= record[start]
                start += 1
                
        res = max(res,end-start+1)
        return res
