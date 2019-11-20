#label: 贪心算法 difficulty: easy

"""

写的代码一直超过时间限制，看了官方解答，算法复杂度和我写的相同，但用了set数据类型，加快了数据检索速度

自己写的代码：

"""

class Solution:
    def robotSim(self, commands, ob):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        origin = [0, 0]
        drection = 40
        result = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        for i in commands:
            if i == -1:
                drection = (drection + 1)%4
            elif i == -2:
                drection = (drection - 1)%4
            else:
                d=drection%4
                for j in range(i):
                    if [origin[0] + dx[d],origin[1] + dy[d]] in ob:
                        break
                    origin = [origin[0] + dx[d],origin[1] + dy[d]]
 
            result = max(pow(origin[0], 2) + pow(origin[1], 2),result)
 
        return result

"""

这个利用list检索，代码运行效率较低，将输入的障碍点改为包含tuple的set类型后，提交通过（创建一个set需要一个list作为书输入），代码如下：

总结：dict及set在检索时速度真的快很多

"""

class Solution:
    def robotSim(self, commands, ob):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        ob= set(map(tuple, ob))
        origin = [0, 0]
        drection = 40
        result = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        for i in commands:
            if i == -1:
                drection = (drection + 1)%4
            elif i == -2:
                drection = (drection - 1)%4
            else:
                d=drection%4
                for j in range(i):
                    if (origin[0] + dx[d],origin[1] + dy[d]) in ob:
                        break
                    origin = [origin[0] + dx[d],origin[1] + dy[d]]
 
            result = max(pow(origin[0], 2) + pow(origin[1], 2),result)
 
        return result

