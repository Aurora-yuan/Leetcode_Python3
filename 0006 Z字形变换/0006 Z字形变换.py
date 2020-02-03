#label: string difficulty: medium

"""
第一种思路：

直白的麻瓜思路，开个数组按顺序一个个压进去，得到上面解释里的数组，然后再从左到右，从上到下读出来就好。

压进去的过程有两种可能，

1. 从上往下压， 定义state = "down"， 每次x += 1，当x触底就转换state为"up"

2. 从左下往右上压， 定义state = "up"， 每次 x -= 1, y += 1， 当x归零就转换state为"down"

"""

class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #麻瓜解法：开个数组，把输入按要求放进去，然后再按输出顺序读出来
        if n <= 1:
            return s
        l = len(s)
        record = [[0] * l for _ in range(n)]
        x, y = 0, 0
        state = "down"
        for i, char in enumerate(s):
            # print x, y, char
            record[x][y] = char
            if state == "down":
                if x != n - 1:
                    x += 1
                else:
                    state = "up"
                    x -= 1
                    y += 1
                continue
            
            elif state == "up":
                if x != 0:
                    x -= 1
                    y += 1
                else:
                    state = "down"
                    x += 1
        # print record
        res = ""
        for row in record:
            for char in row:
                if char != 0:
                    res += char
        
        return res

"""
第二种思路:

找规律。

图见https://blog.csdn.net/qq_32424059/article/details/90080771

"""

class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #找规律
        if n <= 1:
            return s
        l = len(s)
        res = ""
        for i in range(n):
            tmp, index = "", i
            if i in [0, n - 1]:
                while(index < l):
                    
                    tmp += s[index]
                    index += 2 * (n - 1)
            else:
                state = "down"
                while(index < l):
                    tmp += s[index]
                    if state == "down":
                        state = "up"
                        index += 2 * (n - 1 - i)
                    else:
                        state = "down"
                        index += 2 * i
            res += tmp
 
        return res
                    
                        




