#label: array difficulty: easy

"""
常规的话我们弄一个count，看到前一个大于后一个，count 加1，一旦大于1了，自然就是false了。但是这里有一个问题，就是有没有可能，你检测前后，count 只有一次，但是数组其他地方不是单调递增的呢？

解释一下：

count=0
for i in range(len(A)-1)：
    if A[i]>A[i+1]:
         count+=1
 
return count<=1
这个显而易见的方法是错误的，因为下面这个反例：

[2,3,1,2]

如果单个看，只有3比1大， count 只被计数到了一次，但是实际来看，你换3,[2,1,1,2]，不行，换 1, [2,3,2,2],不行，你换一个不会单调递增的，但是count只有一次，显而易见的暴力算法是错误的，这就是这道题tricky 的地方。

但是没关系，既然发现这个tricky的地方，我们就来解决他：看code:

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i>=1 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i]>nums[i+2])):
                    return False
        return True
解释一下：设置一个count, 开始循环，碰到前一个比后一个大的，count +1， 都很strightforward， 好了，当count>1，那么结束了，

解决count 是1 但是不是单调的情况，跟上面那个反例一样，

1）

((i>=1 and nums[i-1]>nums[i+1]) 
首先在第二个数字开始，你当前数字前一个不能大于当前数字后一个

然后:

2）

(i+2<len(nums) and nums[i]>nums[i+2])):
在后面还有2个数字的情况下，你当前数字不能比后面第二个大。还是太抽象，举几个例子吧：

[2,3,1,2] 这种情况下，你怎么调都没用，假设现在到3，当前数字3，前一个2 大于 后一个 1，当前数字3又比后面第二个，2， 大，所以这是错误情况。

条件1和2，两者如果同时满足，数列就不可能靠换一个数字来单调递增。

如果只满足一个呢？

比如 [2,3,1,3]，当前3，前一个2大于后一个1，但是第二条不满足，因为当前没有比后面第二个大，这种情况很显然把1换成3就是单调递增了。

再比如[2,3,2,2],当前3，后面第二个，2，的确比3小，但是第一条不满足，显然换3到2，[2,2,2,2]满足题目要求的。

"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i>=1 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i]>nums[i+2])):
                    return False
        return True


