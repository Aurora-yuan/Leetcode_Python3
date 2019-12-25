#label: dynamic programming difficulty: medium

"""
思路：

依照定义，确实可以通过dfs来逐个交换并且判断。但是时间复杂度是几何上升的。

一般经验是这种可以解决的问题都少不了dp。

但是dp需要一个定义，我们又怎样来定义呢？

所以这里实际上需要两个数组或者说是一组二元变量。

用swap数组中的swap[i]表示第i个元素如果要交换来使得AB成为递增序列那么需要多少次的代价。

用keep数组的keep[i]表示第i个元素不交换使得两个数组依然有序需要多少代价。

举个例子，我们再推导转移方程。

针对A=[1,3,5,7] B=[1,2,3,4]

swap[0]=1,keep[0]=0表示第0个元素为了使其保持有序，交换确实可以，但付出了1次的代价，不交换也可以，0次代价。

这只是初始化，真正的大头在后面。

swap[1]=2,keep[1]=0,这个也很显然，因为只看前两个元素的话，已经是满足条件了。那么如果我非要交换来使得顺序成立，那就需要2次，但是不交换依然可以，0次。

swap[2]=3,keep[2]=0,道理同上一段的推导。

但是swap[3]=1,keep[3]=3，这又是什么道理呢？观察AB的末尾，容易看出其实只要交换了7和4就满足了条件了，那么swap就是1。

但是如果我不想交换这个元素，那么就需要把前三个都交换一次，就是3.

经过上述的推导，我们发现keep[i],swap[i]总是与keep[i-1],swap[i-1]存在着某种联系。

首先有两种情况：

一、第i个元素是满足增序的，也就是A[i]>A[i-1],B[i]>B[i-1]因为只要保持就可以了，所以keep[i]=keep[i-1]，但是如果要交换，

那就比swap[i-1]还多了个第i个元素的代价，也就是swap[i]=swap[i-1]+1.

二、A[i]>B[i-1] 而且B[i]>A[i-1]这种情况满足了“是不是我可以通过交换使得满足条件”，值得一提的是这两个条件应该同时判断，

因为谁也不知道那种情况下会有更小的代价。但是如果交换就会是keep[i-1]+1的代价（因为实际上就是翻转了第i个再加上让前i-1个保持的代价），

同理keep[i]此时等于swap[i-1]因为不翻转这个，但要翻转前i个。

"""

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swap=[0 for x in range(len(A))]
        keep=[0 for x in range(len(A))]
        swap[0]=1
        for i in range(1,len(A)):
            keep[i]=swap[i]=0x7fffffff
            if A[i]>A[i-1] and B[i]>B[i-1]:
                swap[i]=swap[i-1]+1
                keep[i]=keep[i-1]
            if A[i]>B[i-1] and B[i]>A[i-1]:
                keep[i]=min(keep[i],swap[i-1])
                swap[i]=min(swap[i],keep[i-1]+1)
        return min(keep[-1],swap[-1])


