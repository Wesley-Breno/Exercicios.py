class Solution:
    def averageValue(self, nums: list[int]) -> int:
        founded_nums = [n for n in nums if n % 3 == 0 and n % 2 == 0]
        if len(founded_nums) > 0:
            return int(sum(founded_nums) / len(founded_nums))
        return 0
