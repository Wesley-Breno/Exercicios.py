class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        cont_sequences = 0
        for word in words[left:right + 1]:
            if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
                cont_sequences += 1
        return cont_sequences