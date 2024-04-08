class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum([1 for letter in patterns if letter in word])
