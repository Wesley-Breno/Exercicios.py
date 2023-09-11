class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_original = x
        invert_num = 0
        while x > 0:
            lastnum = x % 10
            invert_num = invert_num * 10 + lastnum  # Processes each number
            x //= 10  # Removing last number

        if str(num_original) == str(invert_num):
            return True

        return False
