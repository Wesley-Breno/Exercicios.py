from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        previous_word = ''

        for index, word in enumerate(strs):
            if index == 0:
                previous_word = word

            for letter in word:
            


a = ["flower","flow","flight", 'reup', 'resub']
b = Solution()
c = b.longestCommonPrefix(a)
print(c)