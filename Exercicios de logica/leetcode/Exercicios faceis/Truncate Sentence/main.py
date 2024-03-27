class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        new_word = ''
        for index, word in enumerate(s.split()):
            new_word += ' ' + word
            if index + 1 == k:
                break
        return new_word.strip()
