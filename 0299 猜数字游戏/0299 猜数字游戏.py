#label: string difficulty: easy

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        dict1 = {}
        dict2 = {}
        pos = 0
        neg = 0
        for i,s in enumerate(secret):
            if secret[i] == guess[i]:
                pos += 1
            else:
                if s in dict1:
                    dict1[s] += 1
                else:
                    dict1[s] = 1
                if guess[i] in dict2:
                    dict2[guess[i]] += 1
                else:
                    dict2[guess[i]] = 1
                    
        for key in dict1:
            if key in dict2:
                neg += min(dict1[key],dict2[key])
        
        res = str(pos) + 'A' +str(neg) + 'B'
        return res
