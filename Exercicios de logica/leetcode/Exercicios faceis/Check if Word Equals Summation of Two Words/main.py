from string import ascii_lowercase


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        words = {firstWord: '', secondWord: '', targetWord: ''}

        for word in words:
            for letter in word:
                words[word] += str(ascii_lowercase.index(letter))

        if int(words[firstWord]) + int(words[secondWord]) == int(words[targetWord]):
            return True
        return False
