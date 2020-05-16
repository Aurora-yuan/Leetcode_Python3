#label: dynamic programming difficulty: difficult

"""
https://blog.csdn.net/weixin_42247922/article/details/104420596

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j]表示s的前i个是否能被p的前j个匹配
        m = len(s)+1
        n = len(p)+1
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        for i in range(1,n):
            if p[i-1]=="*":
                dp[0][i] = dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]==s[i-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":
                    # 匹配多次或0次
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m-1][n-1]

