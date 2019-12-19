#label: math difficulty: medium

"""
思路：

每次循环根据k的大小可以确定第一位数，

举例，设n = 3， k = 1， 此时第一位数只可能是1， 2， 3，而且一共有3！ = 6种结果，所以每个数开头对应两种结果

当k = 1或2时，对应的第一位就是1，

当k = 3或4时，对应2，

当k = 5或6时，对应3，

以此类推，可以不断确定第一位的结果。

"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        digit = [i for i in range(1, n + 1)] #生成1 ~ n的列表
        res = ""
        while n > 0:
            tmp = math.factorial(n - 1) #计算一共有多少种组合
            idx =  (k - 1) // tmp #由K在tmp中占的比例来确定第一位的数字
            k -= idx * tmp #第一位确定之后，刷新k
            res += str(digit[idx])
            digit.pop(idx)
            n -= 1
        return res


