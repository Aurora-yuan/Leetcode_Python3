# label: 动态规划 difficulty: easy
"""
解题思路：

利用队列（Queue）数据结构。

将s加入队列，遍历t，当t的当前字符c与队头相同时，将队头弹出。

最后判断队列是否为空即可。
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = collections.deque(s)  #入队
        for c in t:
            if not queue: #队列为空
                return True
            if c == queue[0]:
                queue.popleft()
        return not queue  #队列非空时，not queue = False
