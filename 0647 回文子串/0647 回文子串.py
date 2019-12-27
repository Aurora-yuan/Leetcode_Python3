#label: dynamic programming difficulty: medium

"""
算法：动规

思路：
    联想第5题，用动规记录和求出字符串s的所有是回文串的子字符串，然后用计数器counter技术
    一样也是先从单个字符是回文的dp[i][i]= True开始记录
    再到两个字符dp[i][i+1]  = s[i]==s[i+1]
    再到后面的多个字符的回文dp[i][j] = (dp[i+1][j-1] and s[i+1]==s[j-1])
    还是要注意遍历的方式
    for j in range(1，n)
        for i in range(j-1)
    先从j开始遍历，代表以j结束的子串，然后i再从0开始去循环到j

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        counter = 0
        for i in range(n):
            dp[i][i] = True
            counter += 1
        for i in range(1, n):
            if s[i - 1] == s[i]:
                dp[i - 1][i] = True
                counter += 1
        for j in range(1, n):
            for i in range(j - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    counter += 1
        return counter



