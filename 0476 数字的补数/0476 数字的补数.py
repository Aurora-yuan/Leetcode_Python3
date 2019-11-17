#label: 位运算 difficulty: easy

"""
第一种思路：

最简单的按照题意的思路：

先得到输入的二进制形式，再逐位取反， 最后转回十进制。

"""

class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:] #转换成二进制有“0b”前缀
        b = ""
        for ch in s:
            if ch == "0":
                b += "1"
            else:
                b += "0"
        # print b
        return int(b,2)


“”“
第二种思路：

在将正整数处理为二进制的过程中，如果某一位是0，那么结果就直接加上 2** pos，pos是当前的位置，

这样处理完二进制之后即可直接得到答案。

”“”

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        pos = 0
        while(num >= 2):
            temp = num % 2
            if not temp:
                res += 2 ** pos
            num /= 2
            pos += 1
        return res

