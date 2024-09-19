class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_matrix = len(matrix[0])
        for i in range(len(matrix)):
            for sub in matrix[::-1]:
                matrix[i].append(sub[i])

        for i in range(len(matrix)):
            for c in range(len_matrix):
                matrix[i].pop(0)
