#label: dynamic programming difficulty: medium

"""
思路：

动态规划

用两个变量存双方的战果，用两个指针指取后的结果，不然每次都换新数组有点浪费资源。

然后用一个dp数组存每次取后的结果，奇数存alex结果，偶数存lee结果。

"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        left = 0
        right = len(piles)-1
        dp = [0]*len(piles)
        if(piles[left] > piles[right]):
            dp[0] = piles[left]
            left += 1
        else:
            dp[0] = piles[right]
            right -= 1

        if(piles[left] > piles[right]):
            dp[1] = piles[left]
            left += 1
        else:
            dp[1] = piles[right]
            right -= 1

        i = 2
        while(left < right):
            if(piles[left] > piles[right]):
                dp[i] = dp[i-2] + piles[left]
                left += 1
            else:
                dp[i] = dp[i-2] + piles[right]
                right -= 1
            i += 1
        return dp[-1] < dp[-2]

