#label: array difficulty: easy

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #先排序，再求相邻元素的差
        arr.sort()
        res = list()
        sub = [(arr[m]-arr[m-1]) for m in range(1,len(arr))] 
        minsub = min(sub)
        for t in range(len(sub)):
            if sub[t] == minsub:
                res.append([arr[t],arr[t+1]])
        return res                
