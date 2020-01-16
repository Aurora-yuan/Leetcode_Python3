#label: 二分查找 difficulty: medium

"""
第一种思路：

除法的本质就是被除数不断减去除数 ，当被除数比除数小的时候，被除数就是余数，减法的次数就是商。

所以简单的可以得到下面的代码。

但由于CASE 太大了，逐个减除数比较慢，容易超时，所以需要优化减法的过程。

"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 计算被除数可以减去多少个除数：
        op = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            op = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while(dividend >= divisor):
            dividend -= divisor
            res += 1
            
        INT_MIN = -(2 **31)
        INT_MAX = 2 **31 - 1
        res *= op
        return res if INT_MIN <= res <= INT_MAX else INT_MAX 

"""
第二种思路：

在减法的过程优化一下：

如果是要计算2000 / 2， 那么根据第一种思路，2000要减去1000次2，这显然比较慢，

可以这么计算

2000  - 2 = 1998

1998  - 2 ** 2 = 1994

1994 - 2 ** 3  = 1986

1986 - 2 **4 =  1970

1970 - 2 **5 = 1938

1938 - 2 ** 6 = 1874

1874 - 2 ** 7 = 1746

1746 - 2 **8 = 1490

1490 - 2 **9 = 978

........

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 计算被除数可以减去多少个除数：
        op = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            op = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while(dividend >= divisor):
            multidivisor,multi = divisor,1
            while dividend >= multidivisor:
                dividend -= multidivisor
                res += multi
                multi = multi << 1
                multidivisor = multidivisor << 1
            
        INT_MIN = -(2 **31)
        INT_MAX = 2 **31 - 1
        res *= op
        return res if INT_MIN <= res <= INT_MAX else INT_MAX 



