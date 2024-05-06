class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cont = 0

        while True:
            if num1 == 0 or num2 == 0:
                break

            if num1 < num2:
                num2 -= num1
            else:
                num1 -= num2
            cont += 1

        return cont