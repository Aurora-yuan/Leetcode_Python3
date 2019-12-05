#label: 回溯算法 difficulty: medium

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        candidates.sort()
        def generate(c, t, tmp, s):
            # print s
            if s == target:
                # print tmp
                res.append(tmp[:])
                return
            if s > t:
                return
            for digit in c:
                s = sum(tmp) + digit
                tmp.append(digit)
                generate(c, t, tmp, s) #因为s可能大于target，所以必须要回溯
                tmp.pop()
                
        generate(candidates, target, [], 0)
        #----以下为去重
        for i in range(0, len(res)):
            res[i].sort()
        ress = list()
        
        for i in range(0, len(res)):
            flag = 0 # 1 重复 0 单独
            for j in range(i + 1, len(res)):
                if res[i] == res[j]:
                    flag = 1
                    break
            if not flag:
                ress.append(res[i])
                
        return ress


#大神写的
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        
        def backtrack(remain, temp, start):
            if not remain: #remain为0
                res.append(temp[:])
            else:
                for i, n in enumerate(candidates[start:]):
                    if n > remain:
                        break
                    backtrack(remain-n, temp+[n], start+i)
        backtrack(target, [], 0)
        return res

