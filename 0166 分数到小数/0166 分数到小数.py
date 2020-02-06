#label: string difficulty: medium

"""
解题思路:

使用divmod获取商和余数. 然后通过余数求小数.

不断将余数*10, 再次调用divmod, 则算出来的商就是小数.

如果重复出现小数, 则说明为循环.

"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 求整数
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        fraction = [sign+str(n)]
        if remainder == 0:
            return ''.join(fraction)

        fraction.append('.')
        dic = {}
        # 求小数
        while remainder != 0:
            # 出现过, 则说明进入循环.
            if remainder in dic:
                fraction.insert(dic[remainder], '(')
                fraction.append(')')
                break
            dic[remainder] = len(fraction)
            n, remainder = divmod(remainder*10, abs(denominator))
            fraction.append(str(n))
        return ''.join(fraction)


