#label: rejection sampling difficulty: medium

"""
思路：

利用已有的随机函数rand7将等概率空间扩大，然后从大的等概率空间中取小范围的数。

rand7 - 1的范围是0 ~ 6，每个数出现概率相等，为1/7

（rand7 - 1 ） * 7 的结果是[0, 7, 14, 21, 28, 35, 42]，每个数字出现的概率相等，为1/7

所以 tmp = (rand7()-1)*7 + rand7()-1，得到的数字刚好能均匀覆盖0 ~ 48，

0 ~ 48 就是得到的大的等概率空间，

取0~39这一部分出来，返回%10 +1的结果就是rand10的答案，

如果tmp >=40，那么重新再算。

"""

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            tmp = (rand7()-1)*7 + rand7()-1
            #0 7 14 21 28 35 42
            if tmp < 40:
                return tmp % 10 + 1

