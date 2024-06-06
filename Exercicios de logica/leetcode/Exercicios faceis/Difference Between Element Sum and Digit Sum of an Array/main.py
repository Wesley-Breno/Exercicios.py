class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits = []
        for n in nums:
            if len(str(n)) > 1:
                for digit in str(n):
                    digits.append(int(digit))
            else:
                digits.append(n)
        return sum(nums) - sum(digits)
