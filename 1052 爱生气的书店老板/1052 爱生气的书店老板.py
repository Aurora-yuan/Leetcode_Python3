#label: slide window difficulty: medium

"""
思路：

看到了位置可选的长度为X的一个区间，马上要想到sliding window。

先计算一下假设没有这个不生气BUFF时候每一个长度为X的区间上，可以让多少顾客满意，值为angsum。

再计算有了这个不生气BUFF，在每一个长度为X的区间上，有多少顾客满意，值为presum。

所以对于每个区间，因为这个BUFF而新增的满意顾客数就是presum - angsum，求这个值的最大值即可。

区间和的计算可以用前缀和数组加快计算速度。

"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        record = [0 for _ in range(len(grumpy))] #代表在i满意的顾客总数
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                record[i] += record[i - 1] + customers[i]
            else:
                record[i] += record[i - 1]
                
        tmp =  record[-1]#不生气的时候已经可以满足的
 
        prefix = [0 for _ in range(len(grumpy))]
        prefix[0] = customers[0]
        
        for i in range(1, len(grumpy)):
            prefix[i] += prefix[i - 1] + customers[i]
 
        lo, hi = 0, X - 1
        newcus = 0
        # print prefix
        while(hi < len(grumpy)):
            if lo == 0:
                presum = prefix[hi] - 0 #上了BUFF之后的
                angsum = record[hi] - 0 #没上BUFF
            else:
                presum = prefix[hi] - prefix[lo - 1]
                angsum = record[hi] - record[lo - 1]  
            
            earn = presum - angsum
            # print presum, angsum, earn, hi
            newcus = max(presum - angsum, newcus)
            hi += 1
            lo += 1
        return tmp + newcus
            
            


