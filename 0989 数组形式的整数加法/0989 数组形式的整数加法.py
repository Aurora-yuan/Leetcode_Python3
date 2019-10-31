#label: array difficulty: easy

"""
第一种思路：

都转整数然后相加，Python没有溢出所以可以这么搞。

"""

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        stra = ""
        for digit in A:
            stra += str(digit)
            
        s = str(int(stra) + K)
        
        return [int(x) for x in s]


“”“
第二种思路：

LeetCode-Python-415. 字符串相加

跟415一样，逐位加就好。

”“”

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A = A[::-1]
        B = list()
        while(K):
            K, t = divmod(K, 10)
            B.append(t)
        # print B
        
        l1, l2 = len(A), len(B)
        
        if l1 < l2:#保障l1更长
            l1, l2 = l2, l1
            A, B = B, A
            
        res = [0 for _ in range(l1)]
        for i in range(l1):
            if i < l2:
                res[i] += A[i] + B[i]
            else:
                res[i] += A[i]
            
            while (res[i] > 9):
                res[i] -= 10
                if i != l1 - 1:
                    res[i + 1] += 1
                else:
                    res.append(1)
                    l1 += 1
            
        return res[::-1]
            

