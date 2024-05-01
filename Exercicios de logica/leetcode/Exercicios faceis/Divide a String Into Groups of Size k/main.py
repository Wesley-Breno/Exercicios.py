class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        new_s = []
        while s != '':
            new_s.append(s[:k])
            s = s[k:]

            if k > len(s) > 0:
                s += fill * (k - len(s))
                continue

            if len(s) == 0 and len(new_s[-1]) < k:
                new_s[0] += fill * (k - len(new_s[-1]))
                return new_s

        return new_s
