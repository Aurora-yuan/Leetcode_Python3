#label: maths difficulty: easy

class Solution:
    def binaryGap(self, N: int) -> int:
        b = bin(N)[2:]
        last_one, res = 0, 0  //last_one 记录上一个i出现的位置
        for i, char in enumerate(b):
            if char == "1":
                res = max(res, i - last_one)
                last_one = i
                
        return res

