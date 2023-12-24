class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = [i for i in range(len(s)) if s[i] == c]
        result = [min([abs(i - j) for j in indexes]) for i in range(len(s))]
        return result

