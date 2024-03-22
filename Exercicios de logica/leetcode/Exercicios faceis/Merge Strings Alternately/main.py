class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        response = []

        if len(word1) > len(word2):
            for index, word in enumerate(word1):
                response.append(word)
                try:
                    response.append(word2[index])
                except IndexError:
                    continue

        elif len(word2) > len(word1):
            for index, word in enumerate(word2):
                try:
                    response.append(word1[index])
                except IndexError:
                    ...
                response.append(word)

        else:
            for index, word in enumerate(word1):
                response.append(word)
                response.append(word2[index])

        return ''.join(response)
