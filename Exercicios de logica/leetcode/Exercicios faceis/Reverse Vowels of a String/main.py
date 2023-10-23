class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_correct = []

        for letter in s:
            if letter in vowels:
                vowels_correct.append(letter)

        vowels_reverse = vowels_correct[::-1]

        new_s = ''
        count = 0
        for letter in s:
            if letter in vowels:
                new_s += vowels_reverse[count]
                count += 1
                continue
            new_s += letter

        return new_s