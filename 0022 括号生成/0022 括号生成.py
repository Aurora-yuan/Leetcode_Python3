#label: 回溯算法+剪枝 difficulty: medium

class Solution:
    def generate(self,temp,left,right,result):
        if left == 0 and right == 0:
            result.append(temp)
            return 
        if left > 0:
            self.generate(temp+'(',left-1,right,result)
        if left < right:
            self.generate(temp+')',left,right-1,result)
        
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        self.generate("",n,n,result)
        return result
