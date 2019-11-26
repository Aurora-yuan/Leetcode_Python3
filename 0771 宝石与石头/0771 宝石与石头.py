#label: string difficulty: easy

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for i in S:#字符串可以直接进行迭代
            if i in J:
                count+=1
        return count


