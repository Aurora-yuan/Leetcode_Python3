#label: dictionary difficulty: easy

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        charlist = []
        for i, char in enumerate(licensePlate):
            if char.isalpha():
                t = char
                t = t.lower()
                charlist.append(t)
        charlistrecord = collections.Counter(charlist)
        res = "aaaaaaaaaaaaaaaa"
        
        for word in words:
            cnt = 0
            wordrecord = collections.Counter(word)
            
            for char in charlist:
                if wordrecord.get(char, 0) >= charlistrecord[char]:
                    cnt += 1
            # print word, cnt    
            if cnt == len(charlist): #找完整词
                if len(word) < len(res):
                    res = word
                    
        return res


