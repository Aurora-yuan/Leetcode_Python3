#label: string difficulty: easy

#思路和第415题字符串相加一致

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        elif not b:
            return a
        elif not a and not b:
            return ""
        
        carry,i,j = 0,len(a)-1,len(b)-1
        res = ''
        
        while i>=0 or j>=0 or carry>0:
            if i >= 0:
                carry += ord(a[i]) - ord('0')
            if j >= 0:
                carry += ord(b[j]) - ord('0')
            res += str(carry%2)
            carry = carry // 2
            i -= 1
            j -= 1
        return res[::-1]
            
