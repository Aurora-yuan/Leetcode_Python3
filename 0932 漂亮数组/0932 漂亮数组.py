#label: math difficulty: medium

"""
思路：

这个问题有一个非常美妙的数学解法。首先我们要证明漂亮数组满足这样几种性质

减法（减去一个数仍然是漂亮数组）

(A[k]−x)∗2=A[k]∗2−2∗x 不等于 (A[i]−x+A[j]−x)

乘法（乘上一个数仍然是漂亮数组）

A[k]∗2∗x 不等于 (A[i]+A[j])∗x=A[i]∗x+A[j]∗x

有了上面这两个性质，我们就可以很快解决这个问题了。我们知道一个数组A可以分为奇数部分A1和偶数部分A2。

此时我们如果有一个漂亮数组B，我们根据前面的性质知道2B-1是一个漂亮数组并且是奇数数组，而2B也是一个漂亮数组并且是偶数数组。

那么我们通过2B+2B-1必然可以构成任意一个漂亮数组了。

"""

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        result = [1]
        while len(result) < N:
            result = [2*i-1 for i in result] + [2*j for j in result]
        
        return [i for i in result if i <= N]
