class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits = []
        for num in nums:
            for n in str(num):
                digits.append(int(n))
        return digits