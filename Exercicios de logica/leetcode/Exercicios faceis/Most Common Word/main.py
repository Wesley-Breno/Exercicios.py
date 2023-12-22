from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        for word in paragraph.lower().replace(',', ' ').split(' '):
            sequence_word = ''
            for letter in word:
                if letter.isalpha():
                    sequence_word += letter
            words.append(sequence_word)

        words = [word for word in words if word != '']
        words = dict(sorted(dict(Counter(words)).items(), key=lambda item: item[1], reverse=True))

        for word in words.keys():
            if word not in banned:
                return word