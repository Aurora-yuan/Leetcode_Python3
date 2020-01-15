#label: 分治算法 difficulty: medium

"""
思路：

这是一个典型的大问题可以被铲分为相似的小问题 的问题，所以可以用递归解题，

举例：要计算 1*3 - 2 + 4，

可以被拆成 diffWaysToCompute(1) * diffWaysToCompute(3 - 2 + 4)，

也可以被拆成 diffWaysToCompute(1 * 3) - diffWaysToCompute(2 + 4）

计算出子问题的解之后再根据中间的运算符组合一下：

比如假设左半部分得到的解为[2, 3]，右半部分得到的解为[1,0]，中间的运算符为 加号，

那么组合起来就可以得到[2 + 1, 2+ 0, 3 + 1, 3 + 0]的整体解。

"""

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                
                for l in left:
                    for r in right:
                        if input[i] == "+":
                            res.append(l + r)
                        elif input[i] == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
 
        return res


