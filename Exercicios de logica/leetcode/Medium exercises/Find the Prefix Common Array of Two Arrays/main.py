class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        result = []

        for i in range(len(A)):
            cont = 0
            for n in A[:i + 1]:
                if n in B[:i + 1]:
                    cont += 1
            result.append(cont)

        return result