#label: 动态规划 difficulty: easy
"""
第一种思路：(不推荐)

二维打表法。

简单粗暴，但是会卡在最后一个test case上，内存不够用。
"""
class NumArray(object):
 
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        m = len(nums)
        n = m
        self.dp =[[[0] for _ in range(m)] for i in range(n)]
        
        for i in range(0, m):
            self.dp[i][i] = nums[i]
        
        for i in range(m):
            for j in range(i + 1,n):
                self.dp[i][j] = self.dp[i][j - 1] + nums[j]
 
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[i][j]
        
 
 
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


“”“
第二种思路：（推荐）

优化一下，其实一维打表就够了，用 dp[i] 储存 0 - i 的元素之和，如果求 i - j 的元素之和，就返回dp[j] - dp[i - 1]即可。
”“”

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return None
        n = len(nums)
        self.dp = [0 for _ in range(n)]
        
        self.dp[0] = nums[0]
        
        for i in range(1,n):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        
        else:
            return self.dp[j]-self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
