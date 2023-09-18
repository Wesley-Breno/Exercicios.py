class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for exponent in range(0, 32):
            if 2 ** exponent == n:
                return True
        return False
