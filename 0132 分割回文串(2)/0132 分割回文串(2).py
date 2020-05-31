#label: dynamic programming difficulty: difficult

"""
思路：

动态规划。

状态转移方程：

dp[i] = min(dp[i], dp[j] + 1) if dp[j : i] == dp[j : i][::-1]

"""

class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        #以上是进行预处理，因为testcase大多数答案都是0/1，所以可以加快速度
        
        dp = [i - 1 for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
                    
        return dp[-1]

