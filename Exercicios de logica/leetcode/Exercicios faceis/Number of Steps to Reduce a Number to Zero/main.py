class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        cont = 0
        while True:
            if num % 2 == 0:
                num -= num / 2
            else:
                num -= 1

            cont += 1
            if num == 0:
                break

        return cont