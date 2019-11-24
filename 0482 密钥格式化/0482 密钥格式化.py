#label: string difficulty: easy

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s=S.replace("-",'').upper()
        x=len(s)%K
        res=s[:x]
        for i in range(x,len(s),K):
            if res:
                res+='-'+s[i:i+K]
            else:
                res=s[i:i+K]
        return res

