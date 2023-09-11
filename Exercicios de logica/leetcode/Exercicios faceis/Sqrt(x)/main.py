class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        for num in range(1, x + 1):
            if num * num == x:
                return num
            if num * num > x:
                return num - 1