#label: 位运算 difficulty: easy

class Solution:
    def getSum(self, a: int, b: int) -> int:
        #trick: return sum([a,b])
        #https://www.cnblogs.com/dyzhao-blog/p/5662891.html
        #https://blog.csdn.net/qq_34364995/article/details/80738911
        # while b!=0:
        #     carry=a&b
        #     a=a^b
        #     b=carry<<1
        # return a
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
