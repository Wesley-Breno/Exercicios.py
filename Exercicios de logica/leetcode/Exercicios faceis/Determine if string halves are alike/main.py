class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vogais = ['a', 'e', 'i', 'o', 'u']

        part1 = ''
        part2 = ''
        for i, c in enumerate(s):
            if i >= int(len(s) / 2):
                part2 += c
                continue
            part1 += c

        cont_part1 = len([1 for caractere in part1.lower() if caractere in vogais])
        cont_part2 = len([1 for caractere in part2.lower() if caractere in vogais])

        return True if cont_part1 == cont_part2 else False
