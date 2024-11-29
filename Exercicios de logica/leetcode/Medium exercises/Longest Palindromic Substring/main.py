class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings = []
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i:j][::-1] == s[i:j]:
                    substrings.append(s[i:j])

        maxz = 0
        result = ''

        for i in substrings:
            if len(i) > maxz:
                result = i
                maxz = len(i)

        return result
