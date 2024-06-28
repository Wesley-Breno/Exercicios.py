class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            try:
                s = list(s.partition(part))
                s.remove(part)
                s = ''.join(s)
            except ValueError:
                return ''.join(s)
