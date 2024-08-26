def is_out_of_range(value):
    return value < -2147483648 or value > 2147483647


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if "-" in x:
            x = x.replace("-", '')
            x = '-' + x

        if is_out_of_range(int(x)):
            return 0

        return int(x)
