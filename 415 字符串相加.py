#label: string difficulty: easy

"""
思路一：

最直接的想法，和手算加法的步骤一样，注意进位
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        elif not num2:
            return num1
        elif not num1 and not num2:
            return ""
        
        res = ''
        carry, i, j = 0, len(num1)-1, len(num2)-1
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            res += str(carry%10)
            carry = carry // 10
            i -= 1
            j -= 1
        return res[::-1]


“”“
思路二：

使用字符串表达式
”“”

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval(num1)+eval(num2))#使用字符串表达式

“”“
思路三：

将字符串转化为整数，直接进行加法运算
”“”

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_list=list(num1)#转换成列表
        num2_list=list(num2)
        sum1=sum2=0
        for num in num1_list:
            sum1=sum1*10+int(num)
        for num in num2_list:
            sum2=sum2*10+int(num)
        return str(sum1+sum2)


