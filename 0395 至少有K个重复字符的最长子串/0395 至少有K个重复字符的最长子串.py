#label: recursion difficulty: medium


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/pythonsi-xing-gao-ding-di-gui-xie-fa-by-godcat/
        if len(s) < k:
            return 0
        # 获取出现次数最少的字符
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))
