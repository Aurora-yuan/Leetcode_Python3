#label: 排列 difficulty: medium

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        con = 9 #第一位有9种选择
        for i in range(1,n):
            res += con * (10-i) #第一位9种选择，第二位9种选择，第三位8种选择......
            con *= (10-i)
        return res
        
