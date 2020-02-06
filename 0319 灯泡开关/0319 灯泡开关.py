#label: math difficulty: medium

"""
思路：

首先，因为电灯一开始都是关闭的，所以某一盏灯最后如果是点亮的，必然要被按奇数次开关。

我们假设只有 6 盏灯，而且我们只看第 6 盏灯。需要进行 6 轮操作对吧，请问对于第 6 盏灯，会被按下几次开关呢？这不难得出，

第 1 轮会被按，第 2 轮，第 3 轮，第 6 轮都会被按。

为什么第 1、2、3、6 轮会被按呢？因为 6=1×6=2×3。一般情况下，因子都是成对出现的，也就是说开关被按的次数一般是偶数次。

但是有特殊情况，比如说总共有 16 盏灯，那么第 16 盏灯会被按几次?

16=1×16=2×8=4×4

其中因子 4 重复出现，所以第 16 盏灯会被按 5 次，奇数次。现在你应该理解这个问题为什么和平方根有关了吧？

不过，我们不是要算最后有几盏灯亮着吗，这样直接平方根一下是啥意思呢？稍微思考一下就能理解了。

就假设现在总共有 16 盏灯，我们求 16 的平方根，等于 4，这就说明最后会有 4 盏灯亮着，它们分别是第 1×1=1 盏、第 2×2=4 盏、第 3×3=9 盏和第 4×4=16 盏。

我们不是想求有多少个可开方的数吗，4 是最大的平方根，那么小于 4 的正整数的平方都是在 1~16 内的，是会被按奇数次开关，最终亮着的灯。

就算有的 n 平方根结果是小数，强转成 int 型，也相当于一个最大整数上界，比这个上界小的所有整数，平方后的索引都是最后亮着的灯的索引。

所以说我们直接把平方根转成整数，就是这个问题的答案。

"""

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
