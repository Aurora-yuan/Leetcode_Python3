#label: array difficulty: easy

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        #reshape是numpy.ndarray中的用法，list没有reshape用法
        m, n = len(nums), len(nums[0])
        if m * n != c * r:
            return nums
        
        l = list()
        for row in nums:
            for item in row:
                l.append(item)
        
        cnt = 0
        res = list()
        for i in range(r):
            temp = list()
            for j in range(c):
                temp.append(l[cnt])
                cnt += 1
            res.append(temp)
            
        return res

