class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([sum([1 for num in matrix if num < 0]) for matrix in grid])