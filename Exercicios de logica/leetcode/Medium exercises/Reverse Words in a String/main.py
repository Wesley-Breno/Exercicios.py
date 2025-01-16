import re


class Solution:
    def reverseWords(self, s: str) -> str:
        return re.sub(r"\s+", " ", " ".join(s.split(" ")[::-1]).strip())