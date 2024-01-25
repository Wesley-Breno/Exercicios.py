class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))
        dicionario = {arr_sorted[position]: position + 1 for position in range(len(arr_sorted))}
        return [dicionario[arr[i]] for i in range(len(arr))]
