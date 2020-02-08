#label: array difficulty: medium

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        dic={}
        for i in range(0,n):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        for key in dic:
            if dic[key]>n//3:
                res.append(key)
        return res


