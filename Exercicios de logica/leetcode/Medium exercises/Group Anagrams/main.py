class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        subgroups = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in subgroups.keys():
                subgroups[sorted_word].append(word)
                continue
            subgroups[sorted_word] = [word]
        return list(subgroups.values())