#label: 贪心算法 difficulty: medium

"""
贪心 [Accepted]

想法

我们把 3 个或更多的连续数字称作 chain。

我们从左到右考虑每一个数字 x，如果 x 可以被添加到当前的 chain 中，我们将 x 添加到 chain 中，这一定会比创建一个新的 chain 要更好。

为什么呢？如果我们以 x 为起点新创建一个 chain ，这条新创建更短的链是可以接在之前的链上的，这可能会帮助我们避免创建一个从 x 开始的长度

为 1 或者 2 的短链。

算法

我们将每个数字的出现次数统计好，记 tails[x] 是恰好在 x 之前结束的链的数目。

现在我们逐一考虑每个数字，如果有一个链恰好在 x 之前结束，我们将 x 加入此链中。否则，如果我们可以新建立一条链就新建。

"""
class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True
