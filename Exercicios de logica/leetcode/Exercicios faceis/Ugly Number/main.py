class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        uglys = [2, 3, 5]

        for c in uglys:
            while n % c == 0:
                n /= c

        return n == 1


if __name__ == '__main__':
    obj = Solution()
    # response = obj.isUgly(6)  # True
    response = obj.isUgly(1)  # True
    # response = obj.isUgly(14)  # False
    print(response)
