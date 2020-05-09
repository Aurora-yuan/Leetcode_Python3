#label: 递归 difficulty: difficulty

# https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        match = bool(s) and p[0] in [s[0], "."]
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (match and  self.isMatch(s[1:], p))
        return match and self.isMatch(s[1:], p[1:])
