#label: maths difficulty: easy

"""
思路：

先用字符串的处理得到年月日的数值，

然后判断一下是不是闰年：四年一闰，百年不闰，四百年再闰，

最后根据打表计算。
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        DATE = date.split("-")
        year,month,day = int(DATE[0]),int(DATE[1]),int(DATE[2])
        
        if not year % 400 or (not year % 4 and year % 100):
            days[1] +=1
        return sum(days[:month-1])+day
