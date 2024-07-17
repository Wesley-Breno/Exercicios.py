class Solution:
    def removeStars(self, s: str) -> str:
        while s.find("*") >= 0:
            index = s.find("*")
            s = s[:index - 1] + s[index + 1:]
        return s