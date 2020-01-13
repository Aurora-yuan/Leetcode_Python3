#label: math/dynamic programming difficulty: medium

"""
思路一：

麻瓜思想，每个数转成二进制计数

"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = list()
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res
        
“”“
思路二：
 
《剑指Offer》里提到的结论：如果一个数 i 和 i - 1 做与运算，那么 i 的二进制表示形式中的最右边一个 1 会变成0 。
 
利用动态规划的思想。

如果我们已经知道了 i & i -1 这个数字的1的个数cnt，那么根据上面的提到的结论， i 这个数字中 1 的个数就是 cnt + 1。

所以不难得到状态转移方程： dp[i] = dp[i &  (i - 1)] + 1
 
”“”

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        
        return dp

