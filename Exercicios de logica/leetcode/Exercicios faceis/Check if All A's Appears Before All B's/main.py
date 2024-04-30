class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) == s.count('a') or s.count('a') == 0:
            return True
        first_a = s.find('a')
        last_a = s.rfind('a')
        has_other_letter = [1 if letter != 'a' else 0 for letter in s[first_a:last_a + 1]]
        if 'a' not in s[last_a + 1:] and sum(has_other_letter) == 0 and len(s[:first_a]) == 0:
            return True
        return False
