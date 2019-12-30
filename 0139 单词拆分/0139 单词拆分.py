#label: dynamic programming difficulty: medium

"""
思路：

动态规划，用一个数组record记录切割字符串s时下刀的下标。

每次刷新最远可以拆分的下标，最后判断一下是不是整个字符串都可以被拆分。

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        record = [0]#一开始从开头开始找
        
        for j in range(len(s) + 1):
            for i in record:#在之前每一种找法的基础上找
                if s[i : j] in wordDict: #找到一种可行的分法，说明最远可以拆分到j
                    record.append(j)
                    break
        # print record
        return record[-1] == len(s)


