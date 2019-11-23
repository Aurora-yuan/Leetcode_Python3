#label: pattern match difficulty: easy

"""
思路：

建立一个 str 到pattern的hashmap，用record数组记录一下pattern里每个元素出现的次数

对于str 里的每个word，

如果它本来不在hashmap里，而它对应的pattern小写字母出现次数>0，return False

如果它本来不在hashmap里，而它对应的pattern小写字母也没出现过，说明一切正常，OK， 建立新的映射，并且record记录好

如果它在hashmap里， 而它对应的pattern小写字母和记录里的不一样，return False                     

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(pattern) != len(s):
            return False
        record = [0 for i in range(0, 26)] #记录下pattern里每个字母出现的次数
        hashmap = dict()
        
        for i, word in enumerate(s):
            t = ord(pattern[i]) - ord("a")
            
            if word not in hashmap.keys():
                if record[t] > 0:
                    return False
                hashmap[word] = pattern[i]
                record[t] = 1
            else:
                if hashmap[word] != pattern[i]:
                    return False
                
        return True
                
            

