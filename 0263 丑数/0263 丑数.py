#label: maths difficulty: easy

class Solution:
    def isUgly(self, num: int) -> bool:
        #递归判断 或者 直接把能除2，3，5的全都除完
        if num <= 0 :
            return False
        else:
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
        if num == 1:
            return True
        else:
            return False
