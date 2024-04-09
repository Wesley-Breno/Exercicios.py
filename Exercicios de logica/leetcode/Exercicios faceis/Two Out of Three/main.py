class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        retorning = set()
        all_lists = [nums1, nums2, nums3]
        list_indexes = [[1, 2], [0, 2], [0, 1]]
        for index, lista in enumerate(all_lists):
            for n in lista:
                cont = 1
                for c in range(2):
                    if n in all_lists[list_indexes[index][c]]:
                        cont += 1
                if cont >= 2:
                    retorning.add(n)
        return list(retorning)
