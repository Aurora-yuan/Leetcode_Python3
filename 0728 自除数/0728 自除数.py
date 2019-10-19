#label：maths difficulty: easy

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = list()
        for num in range(left,right+1):
            if num< 10:
                res.append(num)
            else:
                flag = True
                number = str(num)
                for i in number:
                    if int(i)==0 or num % int(i) != 0:
                        flag = False
                        break
                    else:
                        continue
                if flag == True:
                    res.append(num)
        
        return res
