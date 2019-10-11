#label: string difficulty: easy

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        res = []
        T = S.split(" ")
        for index, word in enumerate(T):
            temp = word
            if word[0] in vowel:
                temp += "ma"
            else:
                temp = temp[1:] + temp[0] + "ma"
                
            temp += "a" * (index + 1)           
            res.append(temp)
        
        return " ".join(res)

