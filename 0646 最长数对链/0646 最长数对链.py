#label: 贪心算法 difficulty: medium

"""
思路：

贪心算法，遍历整个数组，每次选择在能够衔接在当前链的末尾且第二个元素最小的数对加入当前数对链。

遍历完数组后可以保证该生成的数对链即是最长的，下面简要的论证该贪心的算法的正确性。

假设目前已找到的一个最长数对链的链头元素为(c1,d1),假设在该数组中存在未被选取加入该数对链的数对(c2,d2)，且d2 < d1。

那么选取(c2,d2)来替换(c1,d1)。由于d2 < d1，新生成的数对链依然合法且仍然是最优解。

所以当一个个从所给数组中挑选能够衔接且有最小的第二个元素数对加入此链时，一定可以在最后得到一个最优解，即最长的数对链

"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda ele:ele[1]) #按照第二个数字排序
        rear, cnt = -sys.maxsize, 0 
        for pair in pairs:
            if pair[0] > rear:
                cnt += 1
                rear = pair[1]
            else:
                continue 
        return cnt  
