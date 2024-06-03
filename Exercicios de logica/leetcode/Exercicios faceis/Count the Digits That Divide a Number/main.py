class Solution:
    def countDigits(self, num: int) -> int:
        return sum([1 for n in str(num) if num % int(n) == 0])
