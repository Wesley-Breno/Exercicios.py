class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        palavras = []
        palavra = ''

        for word in words:
            for row in rows:
                for letter in word:
                    if letter.lower() in row:
                        palavra += letter

                if palavra == word:
                    palavras.append(palavra)
                palavra = ''

        return palavras
