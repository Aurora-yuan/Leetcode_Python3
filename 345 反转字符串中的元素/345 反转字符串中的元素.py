#label: string/双指针 difficulty: easy

"""
双指针法，分别指着左右两个元音字母，然后交换即可，

此题注意字符串不能单独赋值某个元素，需要先将字符串转换成list，最后返回时再将list转换回字符串。
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        s = [char for char in s]
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = l - 1
        while(left < right):
            while(left <= l -1 and s[left] not in vowel):
                left += 1
            while(right >= 0 and s[right] not in vowel):
                right -= 1
            if left < right and s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
