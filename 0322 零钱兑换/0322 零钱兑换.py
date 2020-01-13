#label: dynamic programming difficulty: medium

"""
思路：

动态规划。用dp[i] 表示组成 i 元所需要的最小硬币数。

显然对于coins数组里的所有元素j，所有的dp[j] = 1。

以样例输入一为例：

对于其他的dp[i] = 1 + min(dp[i - 1], dp[i - 2], dp[i - 5])

即求11元的答案可以转化为： 1个一元硬币 + 10元答案 或者 1个两元硬币 + 9元答案 或者1个五元硬币 + 6元答案。

所以dp[i] = 1 + min(dp[i - j]) for j in coins

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = list()
        max_int = 2 << 31
        for i in range(amount + 1):
            if i in coins:
                dp.append(1)
            else:
                dp.append(max_int)
        
        for i in range(amount + 1):
            if i not in coins:
                for j in coins:
                    if i - j > 0:
                        dp[i] = min(dp[i],dp[i-j]+1)
                        
        return dp[amount] if dp[amount] != max_int else -1
