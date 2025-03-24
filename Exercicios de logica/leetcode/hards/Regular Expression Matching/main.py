class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.match(p, s) and re.match(p, s).group() == s:
            return True
        return False