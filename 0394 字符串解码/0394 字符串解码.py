#label: stack/string difficulty: medium

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString  = ""
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif char == ']':
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num * curString
            elif char.isdigit():
                curNum = curNum * 10 + int(char)
            else:
                curString += char
        return curString
