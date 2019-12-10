#label: stack difficulty: medium

"""
思路：

先负后正，不发生碰撞
先正后负，发生碰撞
新建一个栈stack用于存储不发生碰撞以及碰撞完保留下来的行星

当栈顶元素top为正，下一个行星t为负时:
top>-t，结束碰撞
top<-t，top出栈，t继续与栈顶行星碰撞
top==-t，top出栈，结束碰撞

如果t为正：
直接入栈

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            t = asteroids[i]
          
            while stack and stack[-1]>0 and t<0: 
                if stack[-1]<-t:
                    stack.pop()
                    continue
                elif stack[-1] == -t:
                    stack.pop()
                break                        
            else:
                stack.append(t)
            
        return stack
