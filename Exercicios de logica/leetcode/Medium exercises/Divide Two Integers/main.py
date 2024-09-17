import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return 2147483647 if dividend == -2147483648 and divisor == -1 else math.trunc(dividend / divisor)