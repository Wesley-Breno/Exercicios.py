class Solution:
    def sortSentence(self, s: str) -> str:
        ordem = {}

        for word in s.split():
            for letter in word:
                if letter.isdigit():
                    ordem[int(letter)] = ''.join([letter for letter in word if not letter.isdigit()])

        words_dict = dict(sorted(ordem.items()))
        word_ordened = ' '.join([word for key, word in words_dict.items()])
        return word_ordened
