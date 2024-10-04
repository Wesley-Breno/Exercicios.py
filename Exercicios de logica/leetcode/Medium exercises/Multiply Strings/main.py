class Solution:
    def string_to_int(self, s: str) -> int:
        num = 0
        for char in s:
            digit = ord(char) - ord('0')
            num = num * 10 + digit
        return num

    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.string_to_int(num1)
        num2 = self.string_to_int(num2)
        return str(num1 * num2)
