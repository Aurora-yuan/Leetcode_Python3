#label: string difficulty: easy

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moore = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        queue = set()
       
        for word in words:
            temp = ""
            for char in word:
                temp += moore[ord(str(char)) - ord("a")]
            queue.add(temp)
        return len(queue)

