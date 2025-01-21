from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ns = [digit for digit in str(n)]

        for com in permutations(ns, r=len(ns)):
            number = ''.join(com)
            if not number.startswith("0"):
                number = int(number)

                while number > 1:
                    number /= 2

                if number == 1:
                    return True

        return False