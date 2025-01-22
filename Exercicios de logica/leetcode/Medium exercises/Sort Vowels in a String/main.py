class Solution:
    def sortVowels(self, s: str) -> str:
        vogais = ["a", "e", "i", "o", "u"]

        new_s = []
        vogais_in_s = []

        for letter in s:
            if letter.lower() not in vogais:
                new_s.append(letter)
                continue
            new_s.append("*")
            vogais_in_s.append(letter)

        new_s = ''.join(new_s)
        vogais_in_s = sorted(vogais_in_s)

        for v in vogais_in_s:
            new_s = new_s.replace("*", v, 1)

        return new_s