class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alfabeto_completo = 'abcdefghijklmnopqrstuvwxyz'
        letters_values = dict()
        for index, letra in enumerate(alfabeto_completo):
            letters_values[letra] = widths[index]

        soma = 0
        tot_linhas = 0
        last_pixel = 0
        for letter in s:
            soma += letters_values[letter]
            if soma >= 100:
                tot_linhas += 1
                last_pixel = soma
                soma = 0 if soma == 100 else letters_values[letter]

        if soma > 0:
            tot_linhas += 1

        if soma == 0:
            soma = last_pixel

        return [tot_linhas, soma]