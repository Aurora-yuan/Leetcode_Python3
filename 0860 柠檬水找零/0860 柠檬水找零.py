#label: 贪心算法 difficulty: easy

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0 #当前5元和10元的数量
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True


