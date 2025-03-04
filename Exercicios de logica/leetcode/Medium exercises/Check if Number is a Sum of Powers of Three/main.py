class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        numbers = [43046721, 14348907, 4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9,
                   3, 1]
        total = 0
        cont = 0

        notas = {}
        for i in range(0, len(numbers)):
            notas[i] = 0

        while True:
            total += numbers[cont]

            if total > n:
                total -= numbers[cont]
                cont += 1
            else:
                notas[cont] += 1

            if total == n:
                break
            else:
                total += numbers[cont]

                if total > n:
                    total -= numbers[cont]
                else:
                    notas[cont] += 1

        values = []
        for key, value in notas.items():
            if value != 0:
                values.append(value)

        if len(values) == values.count(1):
            return True
        return False