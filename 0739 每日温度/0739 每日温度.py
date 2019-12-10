#label: 单调栈 difficulty: medium

"""
思路：

线性扫描，开辟额外栈，每次扫描的新的元素 T[i] 时，

如果栈为空，就直接将元素下标 i 压到栈里，

如果栈不为空，而且栈顶 s[-1] 对应的气温 T[s[-1] ] 大于等于当前元素 T[i] ，说明气温没有回升，也把元素下标 i 压到栈里

                         而且栈顶 s[-1] 对应的气温 T[s[-1] ] 小于当前元素 T[i] ， 说明气温已经回升，

                         那么对应的天数就是 i - s[-1]， 重复上行和本行直到栈顶元素比当前元素大为止。

"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        s = []
        # print res
        for i in range(0, len(T)):
            while(s and T[i] > T[s[-1]]): #温度回升
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)            
        return res


