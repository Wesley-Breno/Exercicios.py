class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeroes = 0
        while True:
            try:
                nums.pop(nums.index(0))
                count_zeroes += 1
            except ValueError:
                break

        for _ in range(count_zeroes):
            nums.append(0)