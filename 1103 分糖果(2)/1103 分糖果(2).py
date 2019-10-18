#label: maths difficulty: easy

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        round = 0
        while candies>0:
            for i in range(num_people):
                distri = i + 1 + round * num_people
                if candies>=distri:
                    res[i] += distri
                    candies -= distri
                else:
                    res[i] += candies
                    candies = 0
                    break
            round += 1
        return res
                
