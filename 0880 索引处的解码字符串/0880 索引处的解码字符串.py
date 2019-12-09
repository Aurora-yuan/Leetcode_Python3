#label: string difficulty: medium

"""
方法：逆向工作法
思路

如果我们有一个像 appleappleappleappleappleapple 这样的解码字符串和一个像 K=24 这样的索引，那么如果 K=4，答案是相同的。

一般来说，当解码的字符串等于某个长度为 size 的单词重复某些次数（例如 apple 与 size=5 组合重复6次）时，索引 K 的答案与索引 K % size 的答案相同。

我们可以通过逆向工作，跟踪解码字符串的大小来使用这种洞察力。每当解码的字符串等于某些单词 word 重复 d 次时，我们就可以将 k 减少到 K % (Word.Length)。

算法

首先，找出解码字符串的长度。之后，我们将逆向工作，跟踪 size：解析符号 S[0], S[1], ..., S[i] 后解码字符串的长度。

如果我们看到一个数字 S [i]，则表示在解析 S [0]，S [1]，...，S [i-1] 之后解码字符串的大小将是 size / Integer(S[i])。 否则，将是 size - 1。

"""

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

