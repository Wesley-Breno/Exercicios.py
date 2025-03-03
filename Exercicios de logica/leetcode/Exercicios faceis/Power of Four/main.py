from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return log(n, 4).is_integer()