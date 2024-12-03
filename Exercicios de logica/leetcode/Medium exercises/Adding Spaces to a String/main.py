class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        spaces = set(spaces)
        result = ''
        for i, e in enumerate(s):
            if i in spaces:
                result += f' {e}'
            else:
                result += e
        return result