#label: 字符串 difficulty: easy

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans=[0 for i in range(5)]
        for ch in iter(text):
            if ch=='b':
                ans[0]+=1
            elif ch=='a':
                ans[1]+=1
            elif ch=='l':
                ans[2]+=0.5
            elif ch=='o':
                ans[3]+=0.5
            elif ch=='n':
                ans[4]+=1
        return int(min(ans))
