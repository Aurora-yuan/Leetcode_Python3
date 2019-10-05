#label: backtracking difficulty: easy

”“”
第一种思路：
看到题目要求组合或者集合，马上想到可以用回溯法：回溯法本来是说对于每个元素都先考虑放它的情况，再考虑不放它的情况；放在这道题的背景里就是，对于每个字母，先考虑放它，再考虑放它的另一种大小写形式。

用dfs实现回溯，start代表目前从扫描到第几位，

如果是digit，就直接加进去，然后下一层递归

如果是alpha，就先加进去，然后下一层递归；再加对立大小写形式， 然后下一层递归。
“”“

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = list()
        l = len(S)
        if l == 0:
            return [""]
        
        #start表示当前扫描到第几位,temp表示当前的字符串
        def dfs(start,temp):
            if start >= l or len(temp) == l:
                res.append(temp)
                return 
            
            #如果当前位是数字，直接接到字符串后，进行下一层递归
            if S[start].isdigit():
                dfs(start+1,temp+S[start])
                
            #如果当前位是小写字母，就先接到字符串后进行下一层递归；再将其变为大写字母接到字符串后进行下一层递归    
            elif S[start].islower():
                dfs(start+1,temp+S[start])
                dfs(start+1,temp+S[start].upper())
                
            #如果当前位是大写字母，就先接到字符串后进行下一层递归；再将其变为小写字母接到字符串后进行下一层递归     
            elif S[start].isupper():
                dfs(start+1,temp+S[start])
                dfs(start+1,temp+S[start].lower())
            
        dfs(0,"")
        return res
        
        
        
“”“
第二种思路：
除了用DFS回溯实现，我们也可以用BFS来解题， 线性扫描S，

对于扫描到的每个元素， 都把它的大小写形式分别加到，目前的res里的所有结果里，这样可以得到temp，

然后用temp覆盖res。

比如对于S = "a1b2"，

扫描到a时， res = [a, A]

扫描到b时， res = [a1, A1], temp = [a1b, a1B, A1b, A1B]
”“”
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        import copy
        res = [""]
        
        for i, x in enumerate(S):
            if x.isdigit():
                for index, item in enumerate(res):
                    res[index] += (x)
                    
            elif x.isupper():
                temp = list()
                for index, item in enumerate(res):
                    temp.append(item + (x))
                    temp.append(item + (x.lower()))
                res = copy.deepcopy(temp[:])
                
            elif x.islower():
                temp = list()
                for index, item in enumerate(res):
                    temp.append(item + (x))
                    temp.append(item + (x.upper()))       
                res = copy.deepcopy(temp[:])
                
        return res


