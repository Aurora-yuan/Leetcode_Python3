#label: dynamic programming difficulty: medium

"""
第一种思路：

自底向上的动态规划。用dp[i][j] 表示从triangle[i][j]到最后一行的最小路径和。

dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
 
        dp = []        
        for line in triangle:
            temp = []
            for item in line:
                temp.append(0)
            dp.append(temp)
        
        dp[-1] = triangle[-1]
        
        for i in range(l - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
                
        return dp[0][0]
        
"""
进阶的第二种思路：

无需保存中间过程，只要求输出最后第一行的结果，所以可以用一维数组替代二维数组。

逐层向上覆盖中间结果即可。

"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp= triangle[-1]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
                
        return dp[0]
        



