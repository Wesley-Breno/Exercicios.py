from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_count = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in t_count and window[char] == t_count[char]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""
