class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cont = 0
        for word in text.split():
            has_broken_letters = False
            for letter in brokenLetters:
                if letter in word:
                    has_broken_letters = True
            if has_broken_letters is False:
                cont += 1

        return cont
    