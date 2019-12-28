#label: dynamic programming difficulty: medium

"""
思路：

dp[i]表示到第i-1位时解码的方法数
两种情况：
1.s[i-1]单独解码，方法数为dp[i-1]
2.s[i-2:i]拼接成双字符解码，若10<=s[i-2:i]<26，双字符合格，解码的方法数位dp[i-2]，否则为0
综合两种情况，得到状态转移矩阵：
dp[i] = dp[i-1] + (dp[i-2] if 双字符合格 else 0)

为什么dp[i]表示的使i-1位？
例如 216，在判断第二位‘1’时，i-2<0了，状态转移矩阵不能用了，故在前加一位，即dp[0]为1

"""

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(2,n+1):
            if s[i-1]!='0':
                dp[i] = dp[i-1]
             
            if 9< int(s[i-2:i])<27:
                dp[i] += dp[i-2]
            
        return dp[-1]
