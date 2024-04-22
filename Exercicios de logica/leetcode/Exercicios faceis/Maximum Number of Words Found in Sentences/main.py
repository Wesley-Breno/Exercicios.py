class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max([len(word.split()) for word in sentences])
