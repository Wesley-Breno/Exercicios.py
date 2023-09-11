class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_formated = ''
        for word in s.lower():
            if word.isalpha() or word.isdigit():
                word_formated += word

        word_reverse = word_formated[::-1]

        if word_formated == word_reverse:
            return True

        return False
    