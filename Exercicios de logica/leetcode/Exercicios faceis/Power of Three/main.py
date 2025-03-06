class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for exponent in range(0, 32):
            if 3 ** exponent == n:
                return True
        return False