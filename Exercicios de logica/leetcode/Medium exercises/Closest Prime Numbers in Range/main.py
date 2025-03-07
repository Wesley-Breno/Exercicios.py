class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def closestPrimes(self, left: int, right: int) -> list[int]:
        primos = []
        for c in range(left, right+1):
            if self.is_prime(c):
                primos.append(c)

        dicionario = dict()

        while True:
            try:
                dicionario[primos[-1] - primos[-2]] = [primos[-2], primos[-1]]
                primos.pop(-1)

            except IndexError:
                break

        try:
            return dicionario[min(dicionario.keys())]
        except ValueError:
            return [-1, -1]
