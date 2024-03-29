class Solution:
    def replaceDigits(self, s: str) -> str:
        alfabeto = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
        ]

        cont, result = '', ''
        for letra in s:
            if letra.isalpha():
                result += letra
                continue
            cont = int(letra)
            result += alfabeto[alfabeto.index(result[-1]) + cont]

        return result
