# label: BFS difficulty: medium

"""
思路：

单向BFS搜索，

起点是当前单词，下一个点是当前单词可以变换一位得到的新单词，新单词必须满足在wordList里，求从起点到终点的最短路径。

用BFS求解。每一次循环生成当前单词可以变换到的所有单词，再对满足条件的单词进行入队操作。

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        
        if endWord not in wordList or beginWord == endWord:
            return 0
        visited = set()
        wordList = set(wordList)
        
        q = deque()
        q.append([beginWord, 0])
        
        char = "abcdefghijklmnopqrstuvwxyz"
        while q:
            cur, cnt = q.popleft() #从队列里取一个出来
            if cur == endWord: #如果刚好找到了
                return cnt + 1
               
            for i in range(len(cur)):
                for j in range(26):
                    word = cur[:i] + char[j] + cur[i + 1:] #把26种变换可能都生成
                    if word in wordList and word not in visited: #判断变换有没有效
                        visited.add(word)
                        q.append([word, cnt + 1])
                    
        return 0
                    

