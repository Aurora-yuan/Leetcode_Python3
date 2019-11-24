#label: sort difficulty: easy

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        nn=sorted(nums,reverse=True)
        res=[]
        for i in nums:
            if nn.index(i)==0:
                res.append("Gold Medal")
            elif nn.index(i)==1:
                res.append("Silver Medal")
            elif nn.index(i)==2:
                res.append("Bronze Medal")
            else:
                res.append(str(nn.index(i)+1))
        return res


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        hashmap = dict()
        for i, score in enumerate(nums):
            hashmap[score] = i
        nums = sorted(nums, lambda x: -1*x)
        
        mapping = {0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal"} 
        res = [0 for _ in nums]
        for i, score in enumerate(nums):
            if i <= 2: #前三名
                res[hashmap[score]] = mapping[i]
                continue
            
            res[hashmap[score]] = str(i + 1)
            
        return res

