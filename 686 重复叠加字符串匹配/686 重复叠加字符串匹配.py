#label: string difficulty: easy

"""
依题意，需要找到一个正整数n，使得B是A*n的子串，并且n最小，所以并不需要太多繁杂的过程，我们只需要找到n的取值范围，然后正序遍历每个值，如果满足题意
便找到了最小的n，否则不存在这样一个n

nx>=y   这是n取值的下界

nx<=y+(x-1)+(x-1)  这是n取值的上界，因为假若第一个A中最后一个字母是B的第一个字母，并且最后一个A中第一个字母是B的最后一个字母，那么满足n最小，

任意大于这个长度的A*n若满足，则此上界必满足

综合1，2：y/x<=n<=(y+2(x-1))/x

又n为正整数，故  取上整(y/x)<=n<=取下整((y+2(x-1))/x)

"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        x,y=len(A),len(B)
        for i in range(y//x,int((y+2*x-2)//x)+1):
            if (A*i).find(B)!=-1:
                return i
        return -1
