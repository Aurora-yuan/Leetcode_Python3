#label: tree difficulty: medium

"""
思路：

假设n个节点存在二叉排序树的个数是res(n)，

当n = 0时，结果为1，

当n = 1时， 结果为1，

当n = 2时， 结果为2，

当n = 3时， 结果为5，从上面题目的解释里可以看到：

当1是根节点的时候，左子树节点个数（比1小的数的个数）为0，右子树节点个数为 3-1-0 = 2， 所以这种情况的答案总共有res(0) * res(2)，

当2是根节点的时候，左子树节点个数为1， 右子树节点个数为3-1-1 = 1，答案共有res（1） * res(1)

当3是根节点的时候，左子树节点个数为2，右子树节点个数为0，答案共有res(2) * res(0)

所以实际上res(3) = 5 = res(0) * res(2) + res(1) * res(1) + res(2) * res(0)

可得出通项公式res(n) = res(0)*res(n-1) + res(1) * res(n-2) +......+ res(n-2) * res(2) + res(n-1) * res(0)，

即卡特兰数，h(n)=C(2n,n)/(n+1) (n=0,1,2,...)

"""


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i-j-1]
            
        return res[n]


