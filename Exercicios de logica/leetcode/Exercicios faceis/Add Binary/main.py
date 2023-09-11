class Solution:
    def _match_quantity_numbers(self, a: str, b: str) -> list:
        if len(a) < len(b):
            rest = len(b) - len(a)
            a = '0' * rest + a
            return [a, b]

        rest = len(a) - len(b)
        b = '0' * rest + b

        return [a, b]

    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            a, b = self._match_quantity_numbers(a, b)

        result = ''
        bonus = '0'
        b_invertido = ''.join([b[index] for index in range(len(b) - 1, -1, -1)])

        for index, num in enumerate(a[::-1]):
            if bonus == '1':
                if num == '1' and b_invertido[index] == '1':
                    result = '1' + result
                    continue
                if num == '1' and b_invertido[index] == '0' or num == '0' and b_invertido[index] == '1':
                    result = '0' + result
                    continue

                result = '1' + result
                bonus = '0'
                continue

            if num == '1' and b_invertido[index] == '1':
                bonus = '1'
                result = '0' + result
                continue

            if num != b_invertido[index]:
                result = '1' + result
                continue

            result = '0' + result

        if bonus == '1':
            result = '1' + result

        return result
