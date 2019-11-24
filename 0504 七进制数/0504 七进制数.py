#label: math difficulty: easy

class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = []
        if num < 0:
            flag = 1
            num = -num
        else:
            flag = 0
        while num >= 7:
            fig = str(num % 7)
            base7.append(fig)
            num = num // 7
        base7.append(str(num))
        if flag:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)
