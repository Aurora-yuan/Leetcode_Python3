#label: array difficulty: easy

"""
第一种思路：

两种循环暴力法，太慢了过不了最后一个case。
"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(time) - 1):
            for j in range(i + 1, len(time)):
                # print time[i], time[j]
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
                    
        return res

"""
第二种思路：

题目给了每个数的上限为500，所以两数之和的上限为1000，因此可以只要在1000以内的60的倍数里找就行了。

先统计一下每个数出现的频率，然后记录在record这个数组里。

缺点：比较慢，虽然能过但是要700ms。

"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        record = [i * 60 for i in range(1, 18) if i ^ 60 <= 1000]
        # print record
        dic = collections.Counter(time)
        # print dic
        
        res = 0
        for item in time:
            for check in record:
                temp = check - item
                if item == temp:
                    res += dic[temp] - 1
                else:
                    res += dic[temp]
                    
        return res // 2

"""
按照题意，每个数其实等价于它自身 mod 60的结果，所以可以用一个下标从0 - 59 的数组记录一下对应的原始数字的个数。

record[ time[i] % 60 ] += 1。

然后线性扫描， 对于time里的每个数字，在运算前先把自己这一次减掉: record[temp] -= 1， 这是为了避免重复以及满足题目条件 j > i。

然后再加上需要的数字（60 - temp）的个数。

一个特殊情况是，如果temp = 0， 因为余数不会出现60的情况， 无法按上一行的算法进行计算，比如[60, 60, 60]， 但根据中学数学排列组合的思想不难得知，

如果有N个这样的数，那么它们之间任意地取两个共有C N 2 = N * (N - 1) /2 种取法，所以一次计算就可以处理所有的该种情况的数字，

"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1
        
        res = 0
        for i in range(0, len(time)):
            temp = time[i] % 60
 
            if temp:
                record[temp] -= 1
                res += record[60 - temp]
            elif temp == 0 and record[0] > 1:
                # print res, record[0]
                # 5 4+3 +2 +1
                res += record[0] * (record[0] - 1) // 2
                record[0] = 0
 
        return res


"""
第四种思路：

在第三种思路的基础上，进一步优化，

既然我们已经得到了record这个数组，其中记录了整个time数组的元素关于 mod 60 性质的信息，那么我们完全可以仅基于record数组进行计算。

对于一般的数组元素而言，举例：假设record的统计结果为有3个20， 5个40，那么任意地在20里选一个，再在40里选一个，那么就会有15种组成60的结果，15 = （3 * 5 + 5 * 3）/ 2， 3 * 5是以20为主，想要找40时得到结果，以40为主，想要找20则是 5 * 3。由这个例子不难看出，对于普通的数组元素来说， 每一次的组合直接加上record[i] * record[60 - i]就可以了，最后把结果/2 即可。 这么做一定是满足 j > i 的，原因在于每一组组合会重复计算两次，其中必定有一次是满足j > i， 除2的时候保留这一组就行。

对于特殊的数组元素而言，比如 0 和 30， 因为它们需要和自身配对，所以还是用排列组合的思想来处理。

这种思路就比较快了， 50 ms 就可以出结果。

"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1
 
        res = 0
        for i in range(0, 60):
            if i in [0, 30] and record[i] > 1:
                res += record[i] * (record[i] - 1) # 对于0 和 30 来说，在它们中取得所有结果的个数为C N 2 = N *(N - 1) / 2， N是自身统计的个数
                record[i] = 0 # 一次处理完所有的这样的数，然后把record[0]归零，保证不重复计算
            elif i:            
                res += record[60 - i] * record[i]
 
        return res // 2

