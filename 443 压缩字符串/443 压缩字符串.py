#label: string difficulty: easy

"""
思路一：

1.首先构建一个字符串用于存放字符和其重复的次数

2.遍历字符串，碰到连续的字符计算其连续次数，如果连续相同字符的个数大于1则还需要把字符串的次数统计减进去

3.最后把构建好的char_str，list一下并顺序用char_str中的字符改变chars对应位置的字符并返回char_str的长度
 
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        string = ""
        count = 1
        c = len(chars)
        if c == 1:
            return 1
        for i in range(1,c):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    string += chars[i-1] + str(count)
                else:
                    string += chars[i-1]
                count = 1
        if count > 1:
            string += chars[i]+str(count)
        else:
            string += chars[i]
        string = list(string)
        chars[::]=string[::]  #存回本地
        return len(chars)
        
“”“
思路二：

从后向前遍历，这样在压缩的时候就不用更新索引
”“”

class Solution:
    def compress(self, chars: List[str]) -> int:
    
        count = 1
        length = len(chars)
        
        for index in range(length-1, -1, -1):
            if index > 0 and chars[index] == chars[index-1]:
                count += 1
            else:
                end = index + count
                if count == 1:
                    chars[index:end] = [chars[index]]
                else:
                    chars[index:end] = [chars[index]] + list(str(count))
                    count = 1
        
        return len(chars)

