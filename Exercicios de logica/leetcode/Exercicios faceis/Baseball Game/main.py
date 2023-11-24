class Solution:
    def calPoints(self, operations: List[str]) -> int:
        digits = []

        for operation in operations:
            if operation.isdigit() or '-' in operation:
                digits.append(int(operation))
                continue

            if operation == 'C':
                digits = digits[:-1]
                continue

            if operation == 'D':
                digits.append(digits[-1] * 2)
                continue

            if operation == '+':
                digits.append(digits[-1] + digits[-2])

        return sum(digits)
