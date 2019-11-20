#label: 贪心算法 difficulty: easy

"""
第一种思路：

丑陋的暴力解。

"""

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        res = 0
        for i in range(0, n):
            temp = list()
            
            flag = 1 # 1 代表非降序 0 代表降序
            for j in range(0, m):
                if not temp:
                    temp.append(A[j][i])
                elif A[j][i] < temp[-1]:
                    flag = 0
                    break
                else:
                    temp.append(A[j][i])
 
            
            if not flag:
                res +=1
                
        return res

"""
第二种思路：

从评论区学会的 zip（*A）

对于输入：

["cba", "daf", "ghi"]
["zyx", "wvu", "tsr"]

zip（*A）可以非常快地求出列：

[(u'c', u'd', u'g'), (u'b', u'a', u'h'), (u'a', u'f', u'i')]
[(u'z', u'w', u't'), (u'y', u'v', u's'), (u'x', u'u', u'r')]

"""

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        # print zip(*A)
        for col in zip(*A):
            if sorted(col) != list(col):
                res += 1
                
        return res


