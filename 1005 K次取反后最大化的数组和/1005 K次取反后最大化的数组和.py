#label: 贪心算法 difficulty: easy

"""
思路：

首先考虑A中负数的个数M， 如果M 比 K 大，那么只要把最小的M个负数变成正数就可以了，

如果M 比 K 小， 说明光把负数变正还不够，还要考虑处理正数的情况，

先把M个负数都变正，然后判断一下还要做多少次 取相反数 的操作数 K - M，

如果K - M 是个偶数，就说明不用再处理了，因为当前已经没有负数了，取反的操作只会使和保持不变或者减小，直接返回sum(A)就行

如果K - M 是个奇数，就说明至少要做一个取反，就选择最小的元素进行取反。

"""

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        cnt = 0
        for i in A:
            if i < 0:
                cnt += 1
                
        if cnt >= K:
            A.sort()
            s = -1 * sum(A[:K]) + sum(A[K:])
            return s
        
        else:
            temp = K - cnt
            B = list()
            
            for item in A:
                B.append(abs(item))
            # print B   
            B.sort()
            # print sum(B), B
            if temp % 2 == 1:
                return sum(B) - 2* B[0]
            else:
                return sum(B)


