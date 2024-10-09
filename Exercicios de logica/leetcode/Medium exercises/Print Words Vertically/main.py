class Solution:
    def printVertically(self, s: str) -> list[str]:
        response = []
        palavras = s.split(' ')

        while ''.join(palavras) != '':
            try:
                response.append(''.join([palavra[0] for palavra in palavras]))
                palavras = [palavra[1:] for palavra in palavras]

            except IndexError:
                word = ''
                for palavra in palavras:
                    if palavra == '':
                        word += ' '
                        continue
                    word += palavra[0]
                palavras = [palavra[1:] for palavra in palavras]
                response.append(word.rstrip())
                continue

        return response
