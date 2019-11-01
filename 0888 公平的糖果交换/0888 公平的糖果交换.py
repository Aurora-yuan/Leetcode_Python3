#label: array difficulty: easy

"""
思路：

先算出来交换之后的数组的和，然后统计一下B中数字出现的频率，接着遍历A， 对于A中的每一个元素，在B的字典里查找要交换的那个值在不在，如果在就返回。

"""

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:

        from collections import Counter, defaultdict
        sa,sb = sum(A), sum(B)
        s = (sa + sb) // 2 #s是最后每个数组的和
        b = dict(Counter(B))
        t = s - sa
        for item in A:
            temp = item + s - sa # item 对应要换的那个数
            if b.get(temp, 0):
                return [item, temp]


