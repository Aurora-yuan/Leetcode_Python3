#label: slide window difficulty: medium

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_hash = {}
        s2_hash = {}
        for i in range(len(s1)):
            if s1[i] not in s1_hash.keys():
                s1_hash[s1[i]] = 1
            else:
                s1_hash[s1[i]] += 1

            if s2[i] not in s2_hash.keys():
                s2_hash[s2[i]] = 1
            else:
                s2_hash[s2[i]] += 1
        if s2_hash == s1_hash:
            return True
        else:
            left = 0
            right = len(s1)
            while right < len(s2):
                s2_hash[s2[left]] -= 1
                if s2_hash[s2[left]] == 0:
                    s2_hash.pop(s2[left])
                left += 1
                if s2[right] in s2_hash.keys():
                    s2_hash[s2[right]] += 1
                else:
                    s2_hash[s2[right]] = 1
                right += 1
                if s2_hash == s1_hash:
                    return True
        return False
  
#leetcode目前最快、最节省内存的方法
class Solution:
    
    def checkInclusion(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        if s1 == s2:
            return True
        if l2 < l1:
            return False
        s = "abcdefghijklmnopqrstuvwxyz"
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            dict1[s[i]] = 0
            dict2[s[i]] = 0

        for i in range(l1):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        if dict1 == dict2:
            return True

        for i in range(l2 - l1):
            dict2[s2[i]] -= 1
            dict2[s2[i + l1]] += 1
            if dict1 == dict2:
                return True

        return False



