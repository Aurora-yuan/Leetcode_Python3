# label: dictionary difficulty: difficult

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 使用Counter模块来匹配，不会超时
        if not s or not words:
            return []
        length_word = len(words[0])
        length_s = len(s)
        length_words = length_word * len(words)

        result = []
        counter_words = Counter(words)
        for i in range(length_s-length_words+1):
            temp_words = s[i:i+length_words]
            counter_temp_words = []
            for j in range(0,length_words,length_word): # 有步长的话，前面必须加0，否则不对
                counter_temp_words.append(temp_words[j:j+length_word])
            if Counter(counter_temp_words) == counter_words:
                result.append(i)

        return result
            
