class Solution:
    def isHappy(self, n: int) -> bool:
        sum_all = 0
        duplicates = []

        while True:
            digits = [int(digit) for digit in str(n)]

            for i in range(len(digits)):
                sum_all += digits[i] ** 2

            if sum_all in duplicates:
                return False

            if sum_all == 1:
                return True

            duplicates.append(sum_all)
            n = sum_all
            sum_all = 0
