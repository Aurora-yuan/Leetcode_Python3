#label: maths difficulty: easy

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #求数组频数的最大公约数，如果公约数小于2 则是False
        from collections import Counter
        dic = Counter(deck)
        tmp = []
        for v in dic:
            tmp.append(dic[v])
        min_ = min(tmp)
        if min_ < 2:
            return False
        else:
            l = list(set(tmp))
            temp = l[0]
            for value in l:
                if value < 2:
                    return False
                if self.GCD(temp, value) < 2:
                    return False
                temp = self.GCD(temp, value)
            return True

    # 辗转相除法求公约数
    def GCD(self, num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        
        return num1

