class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if len(str(num)) > 1:
                num = sum([int(n) for n in str(num)])
            else:
                return num