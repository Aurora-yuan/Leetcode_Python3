#label: slide window difficulty: hard

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        cnt = collections.Counter(t)
        ans = ''
        n = 0 # 当前我满足了 t 中的字母的种数
        l = 0
        for r, ch in enumerate(s):
            if ch not in cnt: 
                continue
            cnt[ch] -= 1
            if cnt[ch] == 0:
                n += 1
            while s[l] not in cnt or cnt[s[l]] < 0: # 看看当前 l 处的字母是否必要，没必要 l 就加1
                if s[l] in cnt: 
                    cnt[s[l]] += 1
                l += 1
            if n == len(cnt):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l: r+1]
        return ans

