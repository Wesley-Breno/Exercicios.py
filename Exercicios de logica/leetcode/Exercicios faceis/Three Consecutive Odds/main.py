class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cont = 0
        for n in arr:
            if n % 2 != 0:
                cont += 1
                if cont >= 3:
                    return True
                continue
            cont = 0
        return False
