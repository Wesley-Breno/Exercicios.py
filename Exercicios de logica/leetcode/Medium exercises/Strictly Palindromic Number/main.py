class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        base = n - 2
        result = n
        quociente = ''
        while base >= 2:
            quociente += f'{result % base}'
            result = int(result / base)
            if result == 0:
                if quociente == quociente[::-1]:
                    quociente = ''
                    base -= 1
                    result = n
                    continue
                return False
        return True
