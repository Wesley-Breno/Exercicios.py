class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        consecutives = []
        bin_number = str(bin(n)).replace('0b', '')

        for index in range(len(bin_number)):
            if index == 0:
                consecutives.append(bin_number[index])
                continue

            if bin_number[index] == bin_number[index - 1]:
                return False

            consecutives.append(bin_number[index])

        return True
