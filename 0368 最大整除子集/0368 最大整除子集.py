#label: dynamic programming difficulty: medium

"""

思路：

直觉告诉我先排个序是很稳的，但是一般动态规划都是计算什么解的长度，解的最大最小值之类的，突然要返回一个解，还真不会做了。

但是实际上这题动态规划思想非常简单：

排序后，dp【i】是第i个数字结尾的数组段所能拥有的最大整数子集长度。

很显然，dp【i】=max（dp【a1】，dp【a2】。。。dp【ak】）+1，其中dp【ax】代表能实现dp【i】%dp【ax】==0，

也就是说dp【i】是所有在i前面的数字能构造最大整除子集的最长的再加1.

但是单单依靠这个还真的不能解出答案。

参考别人的想法，dp的方程与我的接近，但是用了下标数组来解决解的保存，

让我想起了那个union-find算法，先把坐标设为-1，如果合并两个集合，就把其中一个index【i】=j这样就有i，j合并

所以只要在动态打表时不断地记录下标并且合并交集就可以了

"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp=[0 for x in range(len(nums))]
        index=[-1 for x in range(len(nums))]
        max_len,max_index=0,-1
        for i in range(len(nums)):
            dp[i]=1
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    index[i]=j
                if dp[i]>max_len:
                    max_len=dp[i]
                    max_index=i
        arr=[]
        while True:
            if max_index!=-1:
                arr.append(nums[max_index])
                max_index=index[max_index]
            else:
                break
        return arr[::-1]


