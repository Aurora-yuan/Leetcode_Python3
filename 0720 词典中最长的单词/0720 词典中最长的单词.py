#label: 字典数 difficulty: easy

class Solution:
    def longestWord(self, words: List[str]) -> str:
        #用了一个set集合，判断每个单词的除去倒数第一个字母是否在set里，用一个变量保存最长的单词。
        words.sort()
        tmp=set()
        tmp.add("")
        res=""
        for word in words:
            if word[:-1] in tmp:
                tmp.add(word)
                if len(word)>len(res):
                    res=word
        return res


