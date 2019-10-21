#label: maths difficulty: easy

"""
思路

 正负是一样的，+3和-3需要的最少步数是一样的，可以全部作为正数处理；target不管是是正数还是负数进行的处理都是一样的，唯一的不同就是所有的移动方向都相反，
 比如1-2+3=2和-1+2-3=-2步数一样，只是所有的方向相反。
 要想最少步数达到target，就需要不断向目标前进，就是不断的+，即sum=1+2+3+4+…+n；
 当达到某一步时，刚好sum==target,则步数就是n,大多数情况是sum>target，我们设定dis=sum-target；
 如果dis为偶数，则我们可以通过反转sum=1+2+…+n中某一项的符号，使target=sum，比如dis=4，则反转4/2=2的符号（将+2变为-2，sum值减小了4），也就是说步数还是n；
 如果dis为奇数，则可以让dis继续加上n+1或者n+2，使dis变为偶数，然后就跟dis为偶数的情况一致了，也就是步数为n+1或者n+2(取决于什么时候变为偶数)；

"""

class Solution:
    def reachNumber(self, target: int) -> int:
        sum =0
        step = 0
        target=abs(target)
        while sum<target:
            step +=1
            sum+=step

        dis = sum-target
        if dis%2==0:
            return step
        elif (dis+step+1) % 2 == 0:
            return step + 1
        else:
            return step + 2
