class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for conjunto in nums if len(str(conjunto)) % 2 == 0])
