class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        cont = 1
        while True:
            if cont % 2 == 0 and cont % n == 0:
                return cont
            cont += 1
