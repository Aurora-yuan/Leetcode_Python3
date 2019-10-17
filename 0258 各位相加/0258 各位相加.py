#label: maths difficulty: easy

class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        res = 0
        for i in s:
            res += int(i)
        while res>9:
            s= str(res)
            res = 0
            for i in s:
                res += int(i)
        return res
            
