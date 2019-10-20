#label: maths difficulty: easy

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1 :
            return False
        import math
        s = 1
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                s += i + num // i
       
        return s == num

