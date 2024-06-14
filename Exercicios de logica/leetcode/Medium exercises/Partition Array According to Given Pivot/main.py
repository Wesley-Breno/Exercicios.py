class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivos = [n for n in nums if n == pivot]
        menores = [n for n in nums if n < pivot]
        maiores = [n for n in nums if n > pivot]
        return menores + pivos + maiores
